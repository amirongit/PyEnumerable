from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._queryable import Queryable


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
        comparer: Comparer[TSource],
    ) -> "Queryable[TSource]": ...

    def intersect(
        self,
        second: "Queryable[TSource]",
        /,
        *,
        comparer: Comparer[TSource] | None = None,
    ) -> "Queryable[TSource]": ...

    @overload
    def intersect_by[TKey](
        self,
        second: "Queryable[TKey]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Queryable[TSource]": ...

    @overload
    def intersect_by[TKey](
        self,
        second: "Queryable[TKey]",
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Queryable[TSource]": ...

    def intersect_by[TKey](
        self,
        second: "Queryable[TKey]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> "Queryable[TSource]": ...
