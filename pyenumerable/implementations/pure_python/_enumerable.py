from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable
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
            return max(self.source)  # type: ignore
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
                cast(int, max(enumerated, key=lambda e: e[1])[0])  # type: ignore
            ]
        except TypeError as te:
            msg = (
                "TKey doesn't implement pyenumerable.typing_utility.Comparable"
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
            return min(self.source)  # type: ignore
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
                cast(int, min(enumerated, key=lambda e: e[1])[0])  # type: ignore
            ]
        except TypeError as te:
            msg = (
                "TKey doesn't implement pyenumerable.typing_utility.Comparable"
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
            (any(comparer(item, i) for i in self.source))
            if comparer is not None
            else item in self.source
        )

    def count_(
        self,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> int:
        return (
            sum(1 for i in self.source if predicate(i))
            if predicate is not None
            else len(self.source)
        )

    def single(
        self,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> TSource:
        if (
            len(
                items := tuple(
                    filter(predicate, self.source),
                )
                if predicate is not None
                else self.source,
            )
            != 1
        ):
            msg = (
                "There are zero or more than exactly one item to return; If "
                "predicate is given, make sure it filters exactly one item"
            )
            raise ValueError(msg)
        return items[0]

    def single_or_deafult(
        self,
        default: TSource,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> TSource:
        if (
            length := len(
                items := self.source
                if predicate is None
                else tuple(
                    filter(predicate, self.source),
                ),
            )
        ) > 1:
            msg = (
                "There are more than one item to return or fall back to "
                "default; If predicate is given, make sure it filters one or "
                "zero item"
            )
            raise ValueError(msg)
        return items[0] if length == 1 else default

    def skip(
        self,
        start_or_count: int,
        end: int | None = None,
        /,
    ) -> PurePythonEnumerable[TSource]:
        return PurePythonEnumerable(
            *(
                self.source[:start_or_count] + self.source[end:]
                if (end is not None)
                else self.source[start_or_count:]
            ),
        )

    def skip_last(self, count: int, /) -> PurePythonEnumerable[TSource]:
        return PurePythonEnumerable(*self.source[:-count])

    def skip_while(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> PurePythonEnumerable[TSource]:
        start = 0
        for index, item in enumerate(self.source):
            start = index
            if not predicate(index, item):
                break
        else:
            start += 1
        return PurePythonEnumerable(*self.source[start:])

    def take(
        self,
        start_or_count: int,
        end: int | None = None,
        /,
    ) -> PurePythonEnumerable[TSource]:
        return PurePythonEnumerable(
            *(
                self.source[start_or_count:end]
                if (end is not None)
                else self.source[:start_or_count]
            ),
        )

    def take_last(self, count: int, /) -> PurePythonEnumerable[TSource]:
        return PurePythonEnumerable(*self.source[-count:])

    def take_while(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> PurePythonEnumerable[TSource]:
        stop = 0
        for index, item in enumerate(self.source):
            stop = index
            if not predicate(index, item):
                break
        else:
            stop += 1
        return PurePythonEnumerable(*self.source[:stop])

    def of_type[TResult](
        self,
        type_: type[TResult],
        /,
    ) -> PurePythonEnumerable[TResult]:
        return PurePythonEnumerable(  # type: ignore
            *filter(lambda i: isinstance(i, type_), self.source),
        )

    def all(
        self,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> bool:
        return all(
            (predicate(i) for i in self.source)
            if (predicate is not None)
            else self.source,
        )

    def any(
        self,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> bool:
        return any(
            (predicate(i) for i in self.source)
            if (predicate is not None)
            else self.source,
        )

    def sum(self, /) -> TSource:
        try:
            return sum(self.source)  # type: ignore
        except TypeError as te:
            msg = "TSource can't be passed to bultins.sum"
            raise TypeError(msg) from te

    def where(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> PurePythonEnumerable[TSource]:
        return PurePythonEnumerable(
            *(
                en[1]
                for en in filter(
                    lambda i: predicate(i[0], i[1]),
                    enumerate(self.source),
                )
            ),
        )

    def prepend(
        self,
        element: TSource,
        /,
    ) -> PurePythonEnumerable[TSource]:
        return PurePythonEnumerable(element, *self.source)

    def append(self, element: TSource, /) -> PurePythonEnumerable[TSource]:
        return PurePythonEnumerable(*self.source, element)

    def distinct(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> PurePythonEnumerable[TSource]:
        if len(self.source) == 0:
            return PurePythonEnumerable()

        if comparer is not None:
            out: list[TSource] = []
            for item in self.source:
                for captured in out:
                    if comparer(item, captured):
                        break
                else:
                    out.append(item)
            return PurePythonEnumerable(*out)

        try:
            return PurePythonEnumerable(*dict.fromkeys(self.source).keys())
        except TypeError as te:
            msg = "TSource doesn't implement __hash__; Comparer isn't given"
            raise TypeError(msg) from te


    def distinct_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> PurePythonEnumerable[TSource]:
        if len(self.source) == 0:
            return PurePythonEnumerable()

        if comparer is not None:
            captured_list: list[TSource] = []
            for item in self.source:
                for captured in captured_list:
                    if comparer(key_selector(item), key_selector(captured)):
                        break
                else:
                    captured_list.append(item)
            return PurePythonEnumerable(*captured_list)

        try:
            captured_dict: dict[TKey, TSource] = {}
            for item in self.source:
                if (k := key_selector(item)) not in captured_dict:
                    captured_dict[k] = item

            return PurePythonEnumerable(*captured_dict.values())
        except TypeError as te:
            msg = "TKey doesn't implement __hash__; Comparer isn't given"
            raise TypeError(msg) from te
