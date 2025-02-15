from collections.abc import Callable
from typing import Protocol, overload

from pyenumerable.typing_utility import Comparable, Comparer


class SupportsMin[TSource](Protocol):
    @overload
    def min_(self, /) -> TSource: ...

    @overload
    def min_(self, /, *, comparer: Comparer[TSource]) -> TSource: ...

    @overload
    def min_[TResult](
        self,
        selector: Callable[[TSource], TResult],
        /,
    ) -> TResult: ...

    @overload
    def min_[TResult](
        self,
        selector: Callable[[TSource], TResult],
        /,
        *,
        comparer: Comparer[TResult],
    ) -> TResult: ...

    @overload
    def min_by[TKey: Comparable](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> TSource: ...

    @overload
    def min_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> TSource: ...
