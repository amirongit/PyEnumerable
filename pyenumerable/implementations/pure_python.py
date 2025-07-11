from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable
from contextlib import suppress
from functools import cache
from itertools import chain

from pyenumerable.implementations.utils import assume_not_empty
from pyenumerable.protocol import Associable, Enumerable
from pyenumerable.typing_utility import Comparer


class PurePythonEnumerable[TSource: Hashable](Enumerable[TSource]):
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
        assume_not_empty(self)

        if comparer is not None:
            out = self.source[0]
            for item in self.source[1:]:
                if comparer(item, out):
                    out = item
            return out

        return max(self.source)  # type: ignore

    def max_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> TSource:
        assume_not_empty(self)

        enumerated = enumerate(key_selector(i) for i in self.source)

        if comparer is not None:
            max_key = next(iterable := iter(enumerated))
            for index, key in iterable:
                if comparer(key, max_key[1]):
                    max_key = (index, key)
            return self.source[max_key[0]]

        return self.source[max(enumerated, key=lambda e: e[1])[0]]  # type: ignore

    def min_(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> TSource:
        assume_not_empty(self)

        if comparer is not None:
            out = self.source[0]
            for item in self.source[1:]:
                if comparer(item, out):
                    out = item
            return out

        return min(self.source)  # type: ignore

    def min_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> TSource:
        assume_not_empty(self)

        enumerated = enumerate(key_selector(i) for i in self.source)

        if comparer is not None:
            min_key = next(iterable := iter(enumerated))
            for index, key in iterable:
                if comparer(key, min_key[1]):
                    min_key = (index, key)
            return self.source[min_key[0]]

        return self.source[min(enumerated, key=lambda e: e[1])[0]]  # type: ignore

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
                items := tuple(filter(predicate, self.source))
                if predicate is not None
                else self.source
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
                items := tuple(filter(predicate, self.source))
                if predicate is not None
                else self.source,
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

    def all_(
        self,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> bool:
        return all(
            (predicate(i) for i in self.source)
            if (predicate is not None)
            else self.source,
        )

    def any_(
        self,
        predicate: Callable[[TSource], bool] | None = None,
        /,
    ) -> bool:
        return any(
            (predicate(i) for i in self.source)
            if (predicate is not None)
            else self.source,
        )

    def sum_(self, /) -> TSource:
        return sum(self.source)  # type: ignore

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
        if comparer is not None:
            out: list[TSource] = []
            for item in self.source:
                for captured in out:
                    if comparer(item, captured):
                        break
                else:
                    out.append(item)
            return PurePythonEnumerable(*out)

        return PurePythonEnumerable(*dict.fromkeys(self.source).keys())

    def distinct_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TSource]:
        captured_dict: dict[TKey, TSource] = {}

        if comparer is not None:
            for item in self.source:
                item_key = key_selector(item)
                for captured_key in captured_dict:
                    if comparer(item_key, captured_key):
                        break
                else:
                    captured_dict[item_key] = item
            return PurePythonEnumerable(*captured_dict.values())

        for item in self.source:
            if (item_key := key_selector(item)) not in captured_dict:
                captured_dict[item_key] = item
        return PurePythonEnumerable(*captured_dict.values())

    def order(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> Enumerable[TSource]:
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

        return PurePythonEnumerable(*sorted(self.source))  # type: ignore

    def order_descending(
        self,
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> Enumerable[TSource]:
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

        return PurePythonEnumerable(*sorted(self.source, reverse=True))  # type: ignore

    def order_by[TKey: Hashable](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TSource]:
        cached_selector = cache(key_selector)

        if comparer is not None:
            rank_table: dict[int, list[TSource]] = {}
            for item in self.source:
                rank = 0
                for compared in self.source:
                    if comparer(
                        cached_selector(compared), cached_selector(item)
                    ):
                        rank += 1
                rank_table.setdefault(rank, []).append(item)
            return PurePythonEnumerable(
                from_iterable=[
                    rank_table[key] for key in sorted(rank_table.keys())
                ]
            )

        return PurePythonEnumerable(
            *sorted(self.source, key=cached_selector)  # type: ignore
        )

    def order_by_descending[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TSource]:
        cached_selector = cache(key_selector)

        if comparer is not None:
            rank_table: dict[int, list[TSource]] = {}
            for item in self.source:
                rank = 0
                for compared in self.source:
                    if not comparer(
                        cached_selector(compared), cached_selector(item)
                    ):
                        rank += 1
                rank_table.setdefault(rank, []).append(item)
            return PurePythonEnumerable(
                from_iterable=[
                    rank_table[key] for key in sorted(rank_table.keys())
                ]
            )

        return PurePythonEnumerable(
            *sorted(self.source, key=cached_selector, reverse=True)  # type: ignore
        )

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
        comparer: Comparer[TSource] | None = None,
    ) -> Enumerable[TSource]:
        if self.count_() == 0 or second.count_() == 0:
            return PurePythonEnumerable()

        if comparer is not None:
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

        return PurePythonEnumerable(
            *set(self.source).intersection(second.source)
        )

    def intersect_by[TKey](
        self,
        second: Enumerable[TKey],
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TSource]:
        if self.count_() == 0 or second.count_() == 0:
            return PurePythonEnumerable()

        cached_selector = cache(key_selector)

        if comparer is not None:
            out: list[TSource] = []
            for inner in self.source:
                inner_key = cached_selector(inner)
                for outer_key in second.source:
                    if comparer(inner_key, outer_key):
                        for captured in out:
                            if comparer(inner_key, cached_selector(captured)):
                                break
                        else:
                            out.append(inner)
            return PurePythonEnumerable(*out)

        inner_source_table = {cached_selector(i): i for i in self.source}
        return PurePythonEnumerable(
            *(
                inner_source_table[k]
                for k in (inner_source_table and second.source)
            )
        )

    def sequence_equal(
        self,
        other: Enumerable[TSource],
        /,
        *,
        comparer: Comparer[TSource] = lambda in_, out: in_ == out,
    ) -> bool:
        if self.count_() != other.count_():
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
        comparer: Comparer[TSource] | None = None,
    ) -> Enumerable[TSource]:
        if comparer is not None:
            out: list[TSource] = []
            for inner in self.source:
                for outer in other.source:
                    if comparer(inner, outer):
                        break
                else:
                    out.append(inner)
            return PurePythonEnumerable(*out)

        return PurePythonEnumerable(*set(self.source) - set(other.source))

    def except_by[TKey](
        self,
        other: Enumerable[TSource],
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TSource]:
        if comparer is not None:
            out: list[TSource] = []
            key_table: dict[TSource, TKey] = {}
            for inner in self.source:
                if (inner_key := key_table.get(inner)) is None:
                    inner_key = key_selector(inner)
                    key_table[inner] = inner_key
                for outer in other.source:
                    if (outer_key := key_table.get(outer)) is None:
                        outer_key = key_selector(outer)
                        key_table[outer] = outer_key
                    if comparer(inner_key, outer_key):
                        break
                else:
                    out.append(inner)
            return PurePythonEnumerable(*out)

        inner_key_table = {key_selector(i): i for i in self.source}
        return PurePythonEnumerable(
            *(
                inner_key_table[k]
                for k in inner_key_table.keys()
                - (key_selector(o) for o in other.source)
            )
        )

    def average(self, /) -> float:
        return sum(self.source) / len(self.source)  # type: ignore

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
        assume_not_empty(self)

        curr, start_idx = (
            (seed, 0) if seed is not None else (self.source[0], 1)
        )
        for item in self.source[start_idx:]:
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

        return PurePythonEnumerable(
            *dict.fromkeys((*self.source, *second.source)).keys()
        )

    def union_by[TKey](
        self,
        second: Enumerable[TSource],
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TSource]:
        if comparer is not None:
            out: list[TSource] = []
            key_table: dict[TSource, TKey] = {}
            for inner in self.source:
                if (inner_key := key_table.get(inner)) is None:
                    inner_key = key_selector(inner)
                    key_table[inner] = inner_key
                for captured in out:
                    if comparer(inner_key, key_selector(captured)):
                        break
                else:
                    out.append(inner)
            for outer in second.source:
                if (outer_key := key_table.get(outer)) is None:
                    outer_key = key_selector(outer)
                    key_table[outer] = outer_key
                for captured in out:
                    if comparer(outer_key, key_selector(captured)):
                        break
                else:
                    out.append(outer)
            return PurePythonEnumerable(*out)

        (source_table := {key_selector(i): i for i in self.source}).update(
            {key_selector(o): o for o in second.source}
        )
        return PurePythonEnumerable(*source_table.values())

    def group_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[Associable[TKey, TSource]]:
        cached_selector = cache(key_selector)

        if comparer is not None:
            keys: list[TKey] = []
            values: dict[int, list[TSource]] = {}
            for item in self.source:
                item_key = cached_selector(item)
                for index, k in enumerate(keys):
                    if comparer(k, item_key):
                        values[index].append(item)
                        break
                else:
                    keys.append(item_key)
                    values[len(keys) - 1] = [item]
            return PurePythonEnumerable(
                *(
                    PurePythonAssociable(keys[kid], *v)
                    for kid, v in values.items()
                )
            )

        group_table: dict[TKey, list[TSource]] = {}
        for item in self.source:
            group_table.setdefault(cached_selector(item), []).append(item)
        return PurePythonEnumerable(
            *(
                PurePythonAssociable(k, *values)
                for k, values in group_table.items()
            )
        )

    def join[TInner, TKey, TResult](
        self,
        inner: Enumerable[TInner],
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, TInner], TResult],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TResult]:
        cached_outer_selector = cache(outer_key_selector)
        cached_inner_selector = cache(inner_key_selector)

        if comparer is not None:
            return PurePythonEnumerable(
                *(
                    result_selector(outer_item, inner_item)
                    for outer_item in self.source
                    for inner_item in inner.source
                    if comparer(
                        cached_outer_selector(outer_item),
                        cached_inner_selector(inner_item),
                    )
                )
            )

        inner_table: dict[TKey, list[TInner]] = {}
        for inner_item in inner.source:
            inner_table.setdefault(
                cached_inner_selector(inner_item), []
            ).append(inner_item)
        outer_table: dict[TKey, list[TSource]] = {}
        for outer_item in self.source:
            outer_table.setdefault(
                cached_outer_selector(outer_item), []
            ).append(outer_item)
        return PurePythonEnumerable(
            *(
                result_selector(outer_item, inner_item)
                for k in set(inner_table.keys()).intersection(
                    outer_table.keys()
                )
                for outer_item in outer_table[k]
                for inner_item in inner_table[k]
            )
        )

    def group_join[TInner, TKey, TResult](
        self,
        inner: Enumerable[TInner],
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, Enumerable[TInner]], TResult],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> Enumerable[TResult]:
        if comparer is not None:
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
                *(
                    result_selector(
                        kpair[1], PurePythonEnumerable(*values[index])
                    )
                    for index, kpair in enumerate(keys)
                )
            )

        group_table: dict[TKey, tuple[TSource, list[TInner]]] = {
            outer_key_selector(o): (o, []) for o in self.source
        }
        for inner_item in inner.source:
            with suppress(KeyError):
                group_table[inner_key_selector(inner_item)][1].append(
                    inner_item
                )
        return PurePythonEnumerable(
            *(
                result_selector(values[0], PurePythonEnumerable(*values[1]))
                for values in group_table.values()
            )
        )


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
