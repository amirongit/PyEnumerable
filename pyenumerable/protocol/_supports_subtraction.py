from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsSubtraction[TSource](Protocol):
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
        comparer: Comparer[TSource],
    ) -> "Queryable[TSource]": ...

    def except_(
        self,
        other: "Queryable[TSource]",
        /,
        *,
        comparer: Comparer[TSource] | None = None,
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
        comparer: Comparer[TKey],
    ) -> "Queryable[TSource]": ...

    def except_by[TKey](
        self,
        other: "Queryable[TSource]",
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey] | None = None,
    ) -> "Queryable[TSource]": ...
