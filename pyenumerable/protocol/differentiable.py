from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from .queryable import Queryable


class Differentiable[TSource](Protocol):
    @overload
    def except_(
        self,
        other: "Queryable[TSource]",
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def except_(
        self,
        other: "Queryable[TSource]",
        /,
        *,
        comparer: Callable[[TSource, TSource], bool],
    ) -> "Queryable[TSource]": ...

    def except_(
        self,
        other: "Queryable[TSource]",
        /,
        *,
        comparer: Callable[[TSource, TSource], bool] | None = None,
    ) -> "Queryable[TSource]": ...

    @overload
    def except_by[TKey](
        self,
        other: "Queryable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Queryable[TSource]": ...

    @overload
    def except_by[TKey](
        self,
        other: "Queryable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Callable[[TKey, TKey], bool],
    ) -> "Queryable[TSource]": ...

    def except_by[TKey](
        self,
        other: "Queryable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Callable[[TKey, TKey], bool] | None = None,
    ) -> "Queryable[TSource]": ...
