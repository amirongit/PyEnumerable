from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsIntersect[TSource](Protocol):
    @overload
    def intersect(
        self,
        second: "Enumerable[TSource]",
        /,
    ) -> "Enumerable[TSource]": ...

    @overload
    def intersect(
        self,
        second: "Enumerable[TSource]",
        /,
        *,
        comparer: Comparer[TSource],
    ) -> "Enumerable[TSource]": ...

    @overload
    def intersect_by[TKey](
        self,
        second: "Enumerable[TKey]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[TSource]": ...

    @overload
    def intersect_by[TKey](
        self,
        second: "Enumerable[TKey]",
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Enumerable[TSource]": ...
