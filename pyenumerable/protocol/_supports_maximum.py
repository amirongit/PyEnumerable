from collections.abc import Callable
from typing import Any, Protocol, overload

from pyenumerable.typing_utility import Comparable, Comparer


class SupportsMaximum[TSource](Protocol):
    @overload
    def max_(self, /) -> TSource: ...

    @overload
    def max_(self, /, *, comparer: Comparer[TSource]) -> TSource: ...

    @overload
    def max_[TResult: Comparable](
        self,
        selector: Callable[[TSource], TResult],
        /,
    ) -> TResult: ...

    @overload
    def max_[TResult](
        self,
        selector: Callable[[TSource], TResult],
        /,
        *,
        comparer: Comparer[TResult],
    ) -> TResult: ...

    @overload
    def max_by[TKey: Comparable](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> TSource: ...

    @overload
    def max_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> TSource: ...
