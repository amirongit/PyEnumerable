from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsDistinct[TSource](Protocol):
    @overload
    def distinct(self, /) -> "Enumerable[TSource]": ...

    @overload
    def distinct(
        self,
        /,
        *,
        comparer: Comparer[TSource],
    ) -> "Enumerable[TSource]": ...

    @overload
    def distinct_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Enumerable[TSource]": ...

    @overload
    def distinct_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[TSource]": ...
