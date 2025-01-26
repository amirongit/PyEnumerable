from collections.abc import Callable
from typing import Protocol, overload

from pyenumerable.protocol.enumerable import Enumerable


class Differentiable[TSource](Protocol):
    @overload
    def except_(self, other: Enumerable[TSource]) -> Enumerable[TSource]: ...

    @overload
    def except_(
        self,
        other: Enumerable[TSource],
        comparer: Callable[[TSource, TSource], bool],
    ) -> Enumerable[TSource]: ...

    def except_(
        self,
        other: Enumerable[TSource],
        comparer: Callable[[TSource, TSource], bool] | None = None,
    ) -> Enumerable[TSource]: ...

    @overload
    def except_by[TKey](
        self,
        other: Enumerable[TSource],
        func: Callable[[TSource], TKey],
    ) -> Enumerable[TSource]: ...

    @overload
    def except_by[TKey](
        self,
        other: Enumerable[TSource],
        func: Callable[[TSource], TKey],
        comparer: Callable[[TKey, TKey], bool],
    ) -> Enumerable[TSource]: ...

    def except_by[TKey](
        self,
        other: Enumerable[TSource],
        func: Callable[[TSource], TKey],
        comparer: Callable[[TKey, TKey], bool] | None = None,
    ) -> Enumerable[TSource]: ...
