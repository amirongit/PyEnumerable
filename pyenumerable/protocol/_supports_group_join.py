from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from .queryable import Queryable


class SupportsGroupJoin[TSource](Protocol):
    @overload
    def group_join[TInner, TKey, TResult](
        self,
        inner: "Queryable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, "Queryable[TInner]"], TResult],
        /,
    ) -> "Queryable[TResult]": ...

    @overload
    def group_join[TInner, TKey, TResult](
        self,
        inner: "Queryable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, "Queryable[TInner]"], TResult],
        /,
        *,
        comparer: Callable[[TKey, TKey], bool],
    ) -> "Queryable[TResult]": ...

    def group_join[TInner, TKey, TResult](
        self,
        inner: "Queryable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, "Queryable[TInner]"], TResult],
        /,
        *,
        comparer: Callable[[TKey, TKey], bool] | None = None,
    ) -> "Queryable[TResult]": ...
