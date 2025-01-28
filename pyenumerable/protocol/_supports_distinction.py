from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from .queryable import Queryable


class SupportsDistinction[TSource](Protocol):
    @overload
    def distinct(self, /) -> "Queryable[TSource]": ...

    @overload
    def distinct(
        self,
        /,
        *,
        comparer: Callable[[TSource, TSource], bool],
    ) -> "Queryable[TSource]": ...

    def distinct(
        self,
        /,
        *,
        comparer: Callable[[TSource, TSource], bool] | None = None,
    ) -> "Queryable[TSource]": ...

    @overload
    def distinct_by[TKey](
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
        comparer: Callable[[TKey, TKey], bool],
    ) -> "Queryable[TSource]": ...

    def distinct_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Callable[[TKey, TKey], bool] | None = None,
    ) -> "Queryable[TSource]": ...
