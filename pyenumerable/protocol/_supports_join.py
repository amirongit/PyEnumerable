from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsJoin[TSource](Protocol):
    @overload
    def join[TInner, TKey, TResult](
        self,
        inner: "Queryable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, TInner], TResult],
        /,
    ) -> "Queryable[TResult]": ...

    @overload
    def join[TInner, TKey, TResult](
        self,
        inner: "Queryable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, TInner], TResult],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Queryable[TResult]": ...

    def join[TInner, TKey, TResult](
        self,
        inner: "Queryable[TInner]",
        outer_key_selector: Callable[[TSource], TKey],
        inner_key_selector: Callable[[TInner], TKey],
        result_selector: Callable[[TSource, TInner], TResult],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> "Queryable[TResult]": ...
