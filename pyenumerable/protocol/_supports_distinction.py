from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparable, Comparer

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsDistinction[TSource](Protocol):
    @overload
    def distinct(self, /) -> "Queryable[TSource]": ...

    @overload
    def distinct(
        self,
        /,
        *,
        comparer: Comparer[TSource],
    ) -> "Queryable[TSource]": ...

    @overload
    def distinct_by[TKey: Comparable](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def distinct_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Queryable[TSource]": ...
