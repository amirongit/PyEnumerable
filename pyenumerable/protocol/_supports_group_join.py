from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsGroupJoin[TSource](Protocol):
    @overload
    def group_join[TInner, TKey, TResult](
        self,
        inner: "Enumerable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, "Enumerable[TInner]"], TResult],
        /,
    ) -> "Enumerable[TResult]": ...

    @overload
    def group_join[TInner, TKey, TResult](
        self,
        inner: "Enumerable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, "Enumerable[TInner]"], TResult],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[TResult]": ...
