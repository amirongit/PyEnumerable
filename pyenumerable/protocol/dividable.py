from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from pyenumerable.abc.enumerable import Enumerable


class Dividable[TSource](Protocol):
    @overload
    def distinct(self) -> "Enumerable[TSource]": ...

    @overload
    def distinct(
        self,
        comparer: Callable[[TSource, TSource], bool],
    ) -> "Enumerable[TSource]": ...

    def distinct(
        self,
        comparer: Callable[[TSource, TSource], bool] | None = None,
    ) -> "Enumerable[TSource]": ...

    @overload
    def distinct_by[TKey](
        self,
        func: Callable[[TSource], TKey],
    ) -> "Enumerable[TSource]": ...

    @overload
    def distinct_by[TKey](
        self,
        func: Callable[[TSource], TKey],
        comparer: Callable[[TKey, TKey], bool],
    ) -> "Enumerable[TSource]": ...

    def distinct_by[TKey](
        self,
        func: Callable[[TSource], TKey],
        comparer: Callable[[TKey, TKey], bool] | None = None,
    ) -> "Enumerable[TSource]": ...
