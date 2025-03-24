from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsJoin[TSource](Protocol):
    @overload
    def join[TInner, TKey, TResult](
        self,
        inner: "Enumerable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, TInner], TResult],
        /,
    ) -> "Enumerable[TResult]": ...

    @overload
    def join[TInner, TKey, TResult](
        self,
        inner: "Enumerable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, TInner], TResult],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[TResult]": ...
