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
            max_ = self.source[0]
            for item in self.source[1:]:
                if comparer(item, max_):
                    max_ = item
        else:
            try:
                max_ = max(self.source) # type: ignore
            except TypeError as te:
                msg = (
                    "TSource does't implement "
                    "pyenumerable.typing_utility.Comparable"
                )
                raise TypeError(msg) from te

        return cast(TSource, max_)

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
            max_ = self.source[max_key[0]]
        else:
            try:
                index_of_max = max(enumerated, key=lambda e: e[1])[0] # type: ignore
                max_ = self.source[cast(int, index_of_max)]
            except TypeError as te:
                msg = (
                    "TKey doesn't implement "
                    "pyenumerable.typing_utility.Comparable"
                )
                raise TypeError(msg) from te

        return max_

    def min_(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> TSource:
        PurePythonEnumerable._assume_not_empty(self)
        if comparer is not None:
            min_ = self.source[0]
            for item in self.source[1:]:
                if comparer(item, min_):
                    min_ = item
        else:
            try:
                min_ = min(self.source) # type: ignore
            except TypeError as te:
                msg = (
                    "TSource does't implement "
                    "pyenumerable.typing_utility.Comparable"
                )
                raise TypeError(msg) from te

        return cast(TSource, min_)

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
            min_ = self.source[min_key[0]]
        else:
            try:
                index_of_min = min(enumerated, key=lambda e: e[1])[0] # type: ignore
                min_ = self.source[cast(int, index_of_min)]
            except TypeError as te:
                msg = (
                    "TKey doesn't implement "
                    "pyenumerable.typing_utility.Comparable"
                )
                raise TypeError(msg) from te

        return min_

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
