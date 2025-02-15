from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparable, Comparer

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsUnion[TSource](Protocol):
    @overload
    def union(
        self,
        second: "Queryable[TSource]",
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def union(
        self,
        second: "Queryable[TSource]",
        /,
        *,
        comparer: Comparer[TSource],
    ) -> "Queryable[TSource]": ...

    @overload
    def union_by[TKey: Comparable](
        self,
        second: "Queryable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def union_by[TKey](
        self,
        second: "Queryable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Queryable[TSource]": ...
