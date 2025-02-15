from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparable, Comparer

if TYPE_CHECKING:
    from ._associable import Associable
    from ._enumerable import Enumerable


class SupportsGroupBy[TSource](Protocol):
    @overload
    def group_by[TKey: Comparable, TElement, TResult](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        element_selector: Callable[[TSource], TElement],
        result_selector: Callable[[TKey, "Enumerable[TElement]"], TResult],
    ) -> "Enumerable[TResult]": ...

    @overload
    def group_by[TKey, TElement, TResult](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        element_selector: Callable[[TSource], TElement],
        result_selector: Callable[[TKey, "Enumerable[TElement]"], TResult],
        comparer: Comparer[TKey],
    ) -> "Enumerable[TResult]": ...

    @overload
    def group_by[TKey: Comparable, TElement](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        element_selector: Callable[[TSource], TElement],
    ) -> "Enumerable[Associable[TKey, TElement]]": ...

    @overload
    def group_by[TKey, TElement](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        element_selector: Callable[[TSource], TElement],
        comparer: Comparer[TKey],
    ) -> "Enumerable[Associable[TKey, TElement]]": ...

    @overload
    def group_by[TKey: Comparable, TResult](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        result_selector: Callable[[TKey, "Enumerable[TSource]"], TResult],
    ) -> "Enumerable[TResult]": ...

    @overload
    def group_by[TKey, TResult](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        result_selector: Callable[[TKey, "Enumerable[TSource]"], TResult],
        comparer: Comparer[TKey],
    ) -> "Enumerable[TResult]": ...

    @overload
    def group_by[TKey: Comparable](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Enumerable[Associable[TKey, TSource]]": ...

    @overload
    def group_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[Associable[TKey, TSource]]": ...
