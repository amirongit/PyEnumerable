from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from .associable import Associable
    from .queryable import Queryable


class Groupable[TSource](Protocol):
    @overload
    def group_by[TKey, TElement, TResult](
        self,
        *,
        key_selector: Callable[[TSource], TKey],
        element_selector: Callable[[TSource], TElement],
        result_selector: Callable[[TKey, "Queryable[TElement]"], TResult],
    ) -> "Queryable[TResult]": ...

    @overload
    def group_by[TKey, TElement, TResult](
        self,
        *,
        key_selector: Callable[[TSource], TKey],
        element_selector: Callable[[TSource], TElement],
        result_selector: Callable[[TKey, "Queryable[TElement]"], TResult],
        comparer: Callable[[TKey, TKey], bool],
    ) -> "Queryable[TResult]": ...

    @overload
    def group_by[TKey, TElement](
        self,
        *,
        key_selector: Callable[[TSource], TKey],
        element_selector: Callable[[TSource], TElement],
    ) -> "Queryable[Associable[TKey, TElement]]": ...

    @overload
    def group_by[TKey, TElement](
        self,
        *,
        key_selector: Callable[[TSource], TKey],
        element_selector: Callable[[TSource], TElement],
        comparer: Callable[[TKey, TKey], bool],
    ) -> "Queryable[Associable[TKey, TElement]]": ...

    @overload
    def group_by[TKey, TResult](
        self,
        *,
        key_selector: Callable[[TSource], TKey],
        result_selector: Callable[[TKey, "Queryable[TSource]"], TResult],
    ) -> "Queryable[TResult]": ...

    @overload
    def group_by[TKey, TResult](
        self,
        *,
        key_selector: Callable[[TSource], TKey],
        result_selector: Callable[[TKey, "Queryable[TSource]"], TResult],
        comparer: Callable[[TKey, TKey], bool],
    ) -> "Queryable[TResult]": ...

    @overload
    def group_by[TKey](
        self,
        *,
        key_selector: Callable[[TSource], TKey],
    ) -> "Queryable[Associable[TKey, TSource]]": ...

    @overload
    def group_by[TKey](
        self,
        *,
        key_selector: Callable[[TSource], TKey],
        comparer: Callable[[TKey, TKey], bool],
    ) -> "Queryable[Associable[TKey, TSource]]": ...

    def group_by[TKey, TElement, TResult](
        self,
        *,
        key_selector: Callable[[TSource], TKey] | None = None,
        element_selector: Callable[[TSource], TElement] | None = None,
        result_selector: Callable[
            [TKey, "Queryable[TElement]"],
            TResult,
        ] | None = None,
        comparer: Callable[[TKey, TKey], bool] | None = None,
    ) -> "Queryable[TResult]": ...
