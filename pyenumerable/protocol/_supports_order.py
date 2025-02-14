from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparable, Comparer

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsOrder[TSource](Protocol):
    @overload
    def order(self, /) -> "Queryable[TSource]": ...

    @overload
    def order(
        self,
        comprarer: Comparer[TSource],
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def order_descending(self, /) -> "Queryable[TSource]": ...

    @overload
    def order_descending(
        self,
        comprarer: Comparer[TSource],
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def order_by[TKey: Comparable](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def order_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Queryable[TSource]": ...

    @overload
    def order_by_descending[TKey: Comparable](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def order_by_descending[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Queryable[TSource]": ...
