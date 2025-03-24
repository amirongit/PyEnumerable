from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsExcept[TSource](Protocol):
    @overload
    def except_(
        self,
        other: "Enumerable[TSource]",
        /,
    ) -> "Enumerable[TSource]": ...

    @overload
    def except_(
        self,
        other: "Enumerable[TSource]",
        /,
        *,
        comparer: Comparer[TSource],
    ) -> "Enumerable[TSource]": ...

    @overload
    def except_by[TKey](
        self,
        other: "Enumerable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Enumerable[TSource]": ...

    @overload
    def except_by[TKey](
        self,
        other: "Enumerable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[TSource]": ...
