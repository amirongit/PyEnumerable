from __future__ import annotations

from collections.abc import Callable, Iterable
from itertools import chain
from typing import Any, Protocol, cast

from pyenumerable.typing_utility import Comparer


class PurePythonEnumerable[TSource]:
    def __init__(
        self,
        *items: TSource,
        from_iterable: Iterable[Iterable[TSource]] | None = None,
    ) -> None:
        self._source: tuple[TSource, ...] = items

        if from_iterable is not None:
            self._source += tuple(chain.from_iterable(from_iterable))

    @property
    def source(self) -> tuple[TSource, ...]:
        return self._source

    def select[TResult](
        self,
        selector: Callable[[int, TSource], TResult],
        /,
    ) -> PurePythonEnumerable[TResult]:
        return PurePythonEnumerable(
            *tuple(selector(i, v) for i, v in enumerate(self.source)),
       )

    def select_many[TResult](
        self,
        selector: Callable[[int, TSource], Iterable[TResult]],
        /,
    ) -> PurePythonEnumerable[TResult]:
        return PurePythonEnumerable(
            from_iterable=[selector(i, v) for i, v in enumerate(self.source)],
        )

    def concat(
        self,
        other: PurePythonEnumerable[TSource],
        /,
    ) -> PurePythonEnumerable[TSource]:
        return PurePythonEnumerable(from_iterable=(self.source, other.source))

    def max_(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> TSource:
        PurePythonEnumerable._assume_not_empty(self)
        if comparer is not None:
            out = self.source[0]
            for item in self.source[1:]:
                if comparer(item, out):
                    out = item
            return out

        try:
            return max(self.source) # type: ignore
        except TypeError as te:
            msg = (
                "TSource doesn't implement "
                "pyenumerable.typing_utility.Comparable"
            )
            raise TypeError(msg) from te

    def max_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> TSource:
        PurePythonEnumerable._assume_not_empty(self)
        enumerated = enumerate(key_selector(i) for i in self.source)
        if comparer is not None:
            max_key = next(iterable := iter(enumerated))
            for index, key in iterable:
                if comparer(key, max_key[1]):
                    max_key = (index, key)
            return self.source[max_key[0]]

        try:
            return self.source[
                cast(int, max(enumerated, key=lambda e: e[1])[0]) # type: ignore
            ]
        except TypeError as te:
            msg = (
                "TKey doesn't implement "
                "pyenumerable.typing_utility.Comparable"
            )
            raise TypeError(msg) from te

    def min_(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> TSource:
        PurePythonEnumerable._assume_not_empty(self)
        if comparer is not None:
            out = self.source[0]
            for item in self.source[1:]:
                if comparer(item, out):
                    out = item
            return out

        try:
            return min(self.source) # type: ignore
        except TypeError as te:
            msg = (
                "TSource doesn't implement "
                "pyenumerable.typing_utility.Comparable"
            )
            raise TypeError(msg) from te

    def min_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> TSource:
        PurePythonEnumerable._assume_not_empty(self)
        enumerated = enumerate(key_selector(i) for i in self.source)
        if comparer is not None:
            min_key = next(iterable := iter(enumerated))
            for index, key in iterable:
                if comparer(key, min_key[1]):
                    min_key = (index, key)
            return self.source[min_key[0]]

        try:
            return self.source[
                cast(int, min(enumerated, key=lambda e: e[1])[0]) # type: ignore
            ]
        except TypeError as te:
            msg = (
                    "TKey doesn't implement "
                    "pyenumerable.typing_utility.Comparable"
                    )
            raise TypeError(msg) from te

    @staticmethod
    def _assume_not_empty(instance: PurePythonEnumerable[Any]) -> None:
        if len(instance.source) == 0:
            msg = "Enumerable (self) is empty"
            raise ValueError(msg)

    def contains(
        self,
        item: TSource,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> bool:
        return (
            any(comparer(item, i) for i in self.source)
        ) if comparer is not None else item in self.source

    def count_(
        self,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> int:
        return sum(
            1 for i in self.source if predicate(i)
        ) if predicate is not None else len(self.source)

    def single(
        self,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> TSource:
        if predicate is None and len(self.source) != 1:
            msg = (
                "There is zero or more than exactly one item in "
                "Enumerable (self) and predicate isn't given"
            )
            raise ValueError(msg)

        if predicate is not None:
            if len(result := tuple(filter(predicate, self.source))) != 1:
                msg = (
                    "Zero or more than one items satisfy the given predicate"
                )
                raise ValueError(msg)
            return result[0]

        return self.source[0]

    def single_or_deafult(
        self,
        default: TSource,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> TSource:
        if predicate is None and len(self.source) > 1:
            msg = (
                "There is more than one item in Enumerable (self) and "
                "predicate isn't given"
            )
            raise ValueError(msg)

        if predicate is not None:
            if (
                length := len(
                    filtered := tuple(filter(predicate, self.source)),
                )
            ) > 1:
                msg = (
                    "Zero or more than one items satisfy the given predicate"
                )
                raise ValueError(msg)

            return filtered[0] if length == 1 else default

        try:
            # https://github.com/microsoft/pyright/issues/10051
            return self.source[0] # type: ignore
        except IndexError:
            return default
