from collections.abc import Callable
from typing import Protocol, overload

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
    def max_[TResult: Comparable](
        self,
        selector: Callable[[TSource], TResult],
        /,
        *,
        comparer: Comparer[TResult],
    ) -> TResult: ...

    def max_[TResult: Comparable](
        self,
        selector: Callable[[TSource], TResult] | None = None,
        /,
        *,
        comparer: Comparer[TResult] | Comparer[TSource] | None = None,
    ) -> TResult | TSource: ...
