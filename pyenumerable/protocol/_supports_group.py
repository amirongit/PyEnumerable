from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._associable import Associable
    from ._queryable import Queryable


class SupportsGroup[TSource](Protocol):
    @overload
    def group_by[TKey, TElement, TResult](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        element_selector: Callable[[TSource], TElement],
        result_selector: Callable[[TKey, "Queryable[TElement]"], TResult],
    ) -> "Queryable[TResult]": ...

    @overload
    def group_by[TKey, TElement, TResult](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        element_selector: Callable[[TSource], TElement],
        result_selector: Callable[[TKey, "Queryable[TElement]"], TResult],
        comparer: Comparer[TKey],
    ) -> "Queryable[TResult]": ...

    @overload
    def group_by[TKey, TElement](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        element_selector: Callable[[TSource], TElement],
    ) -> "Queryable[Associable[TKey, TElement]]": ...

    @overload
    def group_by[TKey, TElement](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        element_selector: Callable[[TSource], TElement],
        comparer: Comparer[TKey],
    ) -> "Queryable[Associable[TKey, TElement]]": ...

    @overload
    def group_by[TKey, TResult](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        result_selector: Callable[[TKey, "Queryable[TSource]"], TResult],
    ) -> "Queryable[TResult]": ...

    @overload
    def group_by[TKey, TResult](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        result_selector: Callable[[TKey, "Queryable[TSource]"], TResult],
        comparer: Comparer[TKey],
    ) -> "Queryable[TResult]": ...

    @overload
    def group_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Queryable[Associable[TKey, TSource]]": ...

    @overload
    def group_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Queryable[Associable[TKey, TSource]]": ...

    def group_by[TKey, TElement, TResult](
        self,
        key_selector: Callable[[TSource], TKey] | None = None,
        /,
        *,
        element_selector: Callable[[TSource], TElement] | None = None,
        result_selector: Callable[
            [TKey, "Queryable[TElement]"],
            TResult,
        ] | None = None,
        comparer: Comparer[TKey] | None = None,
    ) -> "Queryable[TResult]": ...
