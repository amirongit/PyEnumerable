from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from pyenumerable.protocol.queryable import Queryable


class SupportsIntersection[TSource](Protocol):
    @overload
    def intersect(
        self,
        second: "Queryable[TSource]",
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def intersect(
        self,
        second: "Queryable[TSource]",
        /,
        *,
        comparer: Callable[[TSource, TSource], bool],
    ) -> "Queryable[TSource]": ...

    def intersect(
        self,
        second: "Queryable[TSource]",
        /,
        *,
        comparer: Callable[[TSource, TSource], bool] | None = None,
    ) -> "Queryable[TSource]": ...

    @overload
    def intersect_by[TKey](
        self,
        second: "Queryable[TKey]",
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def intersect_by[TKey](
        self,
        second: "Queryable[TKey]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Callable[[TKey, TKey], bool],
    ) -> "Queryable[TSource]": ...

    def intersect_by[TKey](
        self,
        second: "Queryable[TKey]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Callable[[TKey, TKey], bool] | None = None,
    ) -> "Queryable[TSource]": ...
