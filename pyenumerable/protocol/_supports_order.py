from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsOrder[TSource](Protocol):
    @overload
    def order(self, /) -> "Enumerable[TSource]": ...

    @overload
    def order(
        self,
        /,
        *,
        comparer: Comparer[TSource],
    ) -> "Enumerable[TSource]": ...

    @overload
    def order_descending(self, /) -> "Enumerable[TSource]": ...

    @overload
    def order_descending(
        self,
        /,
        *,
        comparer: Comparer[TSource],
    ) -> "Enumerable[TSource]": ...

    @overload
    def order_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Enumerable[TSource]": ...

    @overload
    def order_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[TSource]": ...

    @overload
    def order_by_descending[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Enumerable[TSource]": ...

    @overload
    def order_by_descending[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[TSource]": ...
