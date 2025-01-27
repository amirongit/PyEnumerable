from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from pyenumerable.abc.linq import LINQ


class Differentiable[TSource](Protocol):
    @overload
    def except_(self, other: "LINQ[TSource]") -> "LINQ[TSource]": ...

    @overload
    def except_(
        self,
        other: "LINQ[TSource]",
        comparer: Callable[[TSource, TSource], bool],
    ) -> "LINQ[TSource]": ...

    def except_(
        self,
        other: "LINQ[TSource]",
        comparer: Callable[[TSource, TSource], bool] | None = None,
    ) -> "LINQ[TSource]": ...

    @overload
    def except_by[TKey](
        self,
        other: "LINQ[TSource]",
        func: Callable[[TSource], TKey],
    ) -> "LINQ[TSource]": ...

    @overload
    def except_by[TKey](
        self,
        other: "LINQ[TSource]",
        func: Callable[[TSource], TKey],
        comparer: Callable[[TKey, TKey], bool],
    ) -> "LINQ[TSource]": ...

    def except_by[TKey](
        self,
        other: "LINQ[TSource]",
        func: Callable[[TSource], TKey],
        comparer: Callable[[TKey, TKey], bool] | None = None,
    ) -> "LINQ[TSource]": ...
