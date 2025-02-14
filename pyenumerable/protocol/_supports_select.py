from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsSelect[TSource](Protocol):
    def select[TResult](
        self,
        selector: Callable[[int, TSource], TResult],
        /,
    ) -> "Queryable[TResult]": ...

    @overload
    def select_many[TResult](
        self,
        selector: Callable[[int, TSource], Iterable[TResult]],
        /,
    ) -> "Queryable[TResult]": ...

    @overload
    def select_many[TResult, TCollectionItem](
        self,
        iterable_selector: Callable[
            [int, TSource],
            Iterable[TCollectionItem],
        ],
        result_selector: Callable[[TSource, TCollectionItem], TResult],
        /,
    ) -> "Queryable[TResult]": ...
