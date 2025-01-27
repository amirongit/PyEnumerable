from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from pyenumerable.abc.linq import LINQ


class Dividable[TSource](Protocol):
    @overload
    def distinct(self) -> "LINQ[TSource]": ...

    @overload
    def distinct(
        self,
        comparer: Callable[[TSource, TSource], bool],
    ) -> "LINQ[TSource]": ...

    def distinct(
        self,
        comparer: Callable[[TSource, TSource], bool] | None = None,
    ) -> "LINQ[TSource]": ...

    @overload
    def distinct_by[TKey](
        self,
        func: Callable[[TSource], TKey],
    ) -> "LINQ[TSource]": ...

    @overload
    def distinct_by[TKey](
        self,
        func: Callable[[TSource], TKey],
        comparer: Callable[[TKey, TKey], bool],
    ) -> "LINQ[TSource]": ...

    def distinct_by[TKey](
        self,
        func: Callable[[TSource], TKey],
        comparer: Callable[[TKey, TKey], bool] | None = None,
    ) -> "LINQ[TSource]": ...
