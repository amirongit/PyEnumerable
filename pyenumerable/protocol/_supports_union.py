from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsUnion[TSource](Protocol):
    @overload
    def union(
        self,
        second: "Enumerable[TSource]",
        /,
    ) -> "Enumerable[TSource]": ...

    @overload
    def union(
        self,
        second: "Enumerable[TSource]",
        /,
        *,
        comparer: Comparer[TSource],
    ) -> "Enumerable[TSource]": ...

    @overload
    def union_by[TKey](
        self,
        second: "Enumerable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Enumerable[TSource]": ...

    @overload
    def union_by[TKey](
        self,
        second: "Enumerable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[TSource]": ...
