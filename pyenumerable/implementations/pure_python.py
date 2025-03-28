from __future__ import annotations

from collections.abc import Callable, Iterable, Sequence
from contextlib import suppress
from itertools import chain
from typing import Any, Protocol

from pyenumerable.protocol import Associable, Enumerable
from pyenumerable.typing_utility import Comparer


class PurePythonEnumerable[TSource](Enumerable[TSource]):
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
    ) -> Enumerable[TResult]:
        return PurePythonEnumerable(
            *tuple(selector(i, v) for i, v in enumerate(self.source)),
        )

    def select_many[TResult](
        self,
        selector: Callable[[int, TSource], Iterable[TResult]],
        /,
    ) -> Enumerable[TResult]:
        return PurePythonEnumerable(
            from_iterable=[selector(i, v) for i, v in enumerate(self.source)],
        )

    def concat(
        self,
        other: Enumerable[TSource],
        /,
    ) -> Enumerable[TSource]:
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
            return self.source[max(enumerated, key=lambda e: e[1])[0]]  # type: ignore
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
            return self.source[min(enumerated, key=lambda e: e[1])[0]]  # type: ignore
        except TypeError as te:
            msg = (
                "TKey doesn't implement pyenumerable.typing_utility.Comparable"
            )
            raise TypeError(msg) from te

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
    ) -> Enumerable[TSource]:
        return PurePythonEnumerable(
            *(
                self.source[:start_or_count] + self.source[end:]
                if (end is not None)
                else self.source[start_or_count:]
            ),
        )

    def skip_last(self, count: int, /) -> Enumerable[TSource]:
        return PurePythonEnumerable(*self.source[:-count])

    def skip_while(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> Enumerable[TSource]:
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
    ) -> Enumerable[TSource]:
        return PurePythonEnumerable(
            *(
                self.source[start_or_count:end]
                if (end is not None)
                else self.source[:start_or_count]
            ),
        )

    def take_last(self, count: int, /) -> Enumerable[TSource]:
        return PurePythonEnumerable(*self.source[-count:])

    def take_while(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> Enumerable[TSource]:
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
    ) -> Enumerable[TResult]:
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
    ) -> Enumerable[TSource]:
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
    ) -> Enumerable[TSource]:
        return PurePythonEnumerable(element, *self.source)

    def append(self, element: TSource, /) -> Enumerable[TSource]:
        return PurePythonEnumerable(*self.source, element)

    def distinct(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> Enumerable[TSource]:
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
    ) -> Enumerable[TSource]:
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

    def order(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> Enumerable[TSource]:
        if len(self.source) == 0:
            return PurePythonEnumerable()

        if comparer is not None:
            rank_table: dict[int, list[TSource]] = {}
            for item in self.source:
                rank = 0
                for compared in self.source:
                    if comparer(compared, item):
                        rank += 1
                rank_table.setdefault(rank, []).append(item)

            return PurePythonEnumerable(
                from_iterable=[
                    rank_table[key] for key in sorted(rank_table.keys())
                ]
            )

        try:
            return PurePythonEnumerable(*sorted(self.source))  # type: ignore
        except TypeError as te:
            msg = (
                "TSource doesn't implement "
                "pyenumerable.typing_utility.Comparable; Comparer isn't given"
            )
            raise TypeError(msg) from te

    def order_descending(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> Enumerable[TSource]:
        if len(self.source) == 0:
            return PurePythonEnumerable()

        if comparer is not None:
            rank_table: dict[int, list[TSource]] = {}
            for item in self.source:
                rank = 0
                for compared in self.source:
                    if not comparer(compared, item):
                        rank += 1
                rank_table.setdefault(rank, []).append(item)

            return PurePythonEnumerable(
                from_iterable=[
                    rank_table[key] for key in sorted(rank_table.keys())
                ]
            )

        try:
            return PurePythonEnumerable(*sorted(self.source, reverse=True))  # type: ignore
        except TypeError as te:
            msg = (
                "TSource doesn't implement "
                "pyenumerable.typing_utility.Comparable; Comparer isn't given"
            )
            raise TypeError(msg) from te

    def order_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TSource]:
        if len(self.source) == 0:
            return PurePythonEnumerable()

        if comparer is not None:
            rank_table: dict[int, list[TSource]] = {}
            for item in self.source:
                rank = 0
                item_key = key_selector(item)
                for compared in self.source:
                    if comparer(key_selector(compared), item_key):
                        rank += 1
                rank_table.setdefault(rank, []).append(item)

            return PurePythonEnumerable(
                from_iterable=[
                    rank_table[key] for key in sorted(rank_table.keys())
                ]
            )

        try:
            return PurePythonEnumerable(
                *sorted(self.source, key=key_selector)  # type: ignore
            )
        except TypeError as te:
            msg = (
                "TSource doesn't implement "
                "pyenumerable.typing_utility.Comparable; Comparer isn't given"
            )
            raise TypeError(msg) from te

    def order_by_descending[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TSource]:
        if len(self.source) == 0:
            return PurePythonEnumerable()

        if comparer is not None:
            rank_table: dict[int, list[TSource]] = {}
            for item in self.source:
                rank = 0
                item_key = key_selector(item)
                for compared in self.source:
                    if not comparer(key_selector(compared), item_key):
                        rank += 1
                rank_table.setdefault(rank, []).append(item)

            return PurePythonEnumerable(
                from_iterable=[
                    rank_table[key] for key in sorted(rank_table.keys())
                ]
            )

        try:
            return PurePythonEnumerable(
                *sorted(self.source, key=key_selector, reverse=True)  # type: ignore
            )
        except TypeError as te:
            msg = (
                "TSource doesn't implement "
                "pyenumerable.typing_utility.Comparable; Comparer isn't given"
            )
            raise TypeError(msg) from te

    def zip[TSecond](
        self,
        second: Enumerable[TSecond],
        /,
    ) -> Enumerable[tuple[TSource, TSecond]]:
        return PurePythonEnumerable(*zip(self.source, second.source))

    def reverse(self, /) -> Enumerable[TSource]:
        return PurePythonEnumerable(*reversed(self.source))

    def intersect(
        self,
        second: Enumerable[TSource],
        /,
        *,
        comparer: Comparer[TSource] = lambda in_, out: in_ == out,
    ) -> Enumerable[TSource]:
        if len(self.source) == 0 or len(second.source) == 0:
            return PurePythonEnumerable()
        out: list[TSource] = []
        for inner in self.source:
            for outer in second.source:
                if comparer(inner, outer):
                    for captured in out:
                        if comparer(inner, captured):
                            break
                    else:
                        out.append(inner)
        return PurePythonEnumerable(*out)

    def intersect_by[TKey](
        self,
        second: Enumerable[TKey],
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] = lambda in_, out: in_ == out,
    ) -> Enumerable[TSource]:
        if len(self.source) == 0 or len(second.source) == 0:
            return PurePythonEnumerable()
        out: list[TSource] = []
        for inner in self.source:
            inner_key = key_selector(inner)
            for outer_key in second.source:
                if comparer(inner_key, outer_key):
                    for captured in out:
                        captured_key = key_selector(captured)
                        if comparer(inner_key, captured_key):
                            break
                    else:
                        out.append(inner)
        return PurePythonEnumerable(*out)

    def sequence_equal(
        self,
        other: Enumerable[TSource],
        /,
        *,
        comparer: Comparer[TSource] = lambda in_, out: in_ == out,
    ) -> bool:
        if len(self.source) != len(other.source):
            return False
        return all(
            comparer(inner, outer)
            for inner, outer in zip(self.source, other.source)
        )

    def except_(
        self,
        other: Enumerable[TSource],
        /,
        *,
        comparer: Comparer[TSource] = lambda in_, out: in_ == out,
    ) -> Enumerable[TSource]:
        out: list[TSource] = []
        for inner in self.source:
            for outer in other.source:
                if comparer(inner, outer):
                    break
            else:
                out.append(inner)
        return PurePythonEnumerable(*out)

    def except_by[TKey](
        self,
        other: Enumerable[TSource],
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] = lambda in_, out: in_ == out,
    ) -> Enumerable[TSource]:
        out: list[TSource] = []
        for inner in self.source:
            inner_key = key_selector(inner)
            for outer in other.source:
                if comparer(inner_key, key_selector(outer)):
                    break
            else:
                out.append(inner)
        return PurePythonEnumerable(*out)

    def average(self, /) -> float:
        try:
            return sum(self.source) / len(self.source)  # type: ignore
        except TypeError as te:
            msg = "Average can't be executed on TSource"
            raise TypeError(msg) from te

    def chunk(self, size: int, /) -> tuple[PurePythonEnumerable[TSource], ...]:
        return tuple(
            PurePythonEnumerable(*c)
            for c in (
                self.source[i : i + size]
                for i in range(0, len(self.source), size)
            )
        )

    def aggregate(
        self,
        func: Callable[[TSource, TSource], TSource],
        /,
        *,
        seed: TSource | None = None,
    ) -> TSource:
        PurePythonEnumerable._assume_not_empty(self)
        curr, start = (seed, 0) if seed is not None else (self.source[0], 1)
        for item in self.source[start:]:
            curr = func(curr, item)
        return curr

    def union(
        self,
        second: Enumerable[TSource],
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> Enumerable[TSource]:
        if comparer is not None:
            out: list[TSource] = []
            for inner in self.source:
                for captured in out:
                    if comparer(inner, captured):
                        break
                else:
                    out.append(inner)
            for outer in second.source:
                for captured in out:
                    if comparer(outer, captured):
                        break
                else:
                    out.append(outer)
            return PurePythonEnumerable(*out)
        try:
            return PurePythonEnumerable(
                *dict.fromkeys((*self.source, *second.source)).keys()
            )
        except TypeError as te:
            msg = "TSource doesn't implement __hash__; Comparer isn't given"
            raise TypeError(msg) from te

    def union_by[TKey](
        self,
        second: Enumerable[TSource],
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] = lambda in_, out: in_ == out,
    ) -> Enumerable[TSource]:
        out: list[TSource] = []
        for inner in self.source:
            inner_key = key_selector(inner)
            for captured in out:
                if comparer(inner_key, key_selector(captured)):
                    break
            else:
                out.append(inner)
        for outer in second.source:
            outer_key = key_selector(outer)
            for captured in out:
                if comparer(outer_key, key_selector(captured)):
                    break
            else:
                out.append(outer)
        return PurePythonEnumerable(*out)

    def group_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] = lambda in_, out: in_ == out,
    ) -> Enumerable[Associable[TKey, TSource]]:
        keys: list[TKey] = []
        values: dict[int, list[TSource]] = {}
        for item in self.source:
            item_key = key_selector(item)
            for index, k in enumerate(keys):
                if comparer(k, item_key):
                    values[index].append(item)
                    break
            else:
                keys.append(item_key)
                values[len(keys) - 1] = [item]
        return PurePythonEnumerable(
            *(PurePythonAssociable(keys[kid], *v) for kid, v in values.items())
        )

    def join[TInner, TKey, TResult](
        self,
        inner: Enumerable[TInner],
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, TInner], TResult],
        /,
        *,
        comparer: Comparer[TKey] = lambda out, in_: out == in_,
    ) -> Enumerable[TResult]:
        out: list[TResult] = []
        for outer_item in self.source:
            outer_key = outer_key_selector(outer_item)
            for inner_item in inner.source:
                if comparer(outer_key, inner_key_selector(inner_item)):
                    out.append(result_selector(outer_item, inner_item))  # noqa: PERF401
        return PurePythonEnumerable(*out)

    def group_join[TInner, TKey, TResult](
        self,
        inner: Enumerable[TInner],
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, Enumerable[TInner]], TResult],
        /,
        *,
        comparer: Comparer[TKey] = lambda out, in_: out == in_,
    ) -> Enumerable[TResult]:
        keys: list[tuple[TKey, TSource]] = []
        values: dict[int, list[TInner]] = {}
        for outer_item in self.source:
            outer_key = outer_key_selector(outer_item)
            for index, kpair in enumerate(keys):
                if comparer(outer_key, kpair[0]):
                    break
            else:
                keys.append((outer_key, outer_item))
                values[len(keys) - 1] = []
        for inner_item in inner.source:
            inner_key = inner_key_selector(inner_item)
            for index, kpair in enumerate(keys):
                if comparer(kpair[0], inner_key):
                    values[index].append(inner_item)
        return PurePythonEnumerable(
            *[
                result_selector(kpair[1], PurePythonEnumerable(*values[index]))
                for index, kpair in enumerate(keys)
            ]
        )

    @staticmethod
    def _assume_not_empty(instance: PurePythonEnumerable[Any]) -> None:
        if len(instance.source) == 0:
            msg = "Enumerable (self) is empty"
            raise ValueError(msg)


class PurePythonAssociable[TKey, TSource](
    Associable[TKey, TSource],
    PurePythonEnumerable[TSource],
):
    def __init__(
        self,
        key: TKey,
        *items: TSource,
        from_iterable: Iterable[Iterable[TSource]] | None = None,
    ) -> None:
        self._key = key
        super().__init__(*items, from_iterable=from_iterable)

    @property
    def key(self) -> TKey:
        return self._key
