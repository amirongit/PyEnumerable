from collections.abc import Callable
from typing import Protocol, overload


class SupportsExistenceCheck[TSource](Protocol):
    @overload
    def contains(
        self,
        item: TSource,
        /,
    ) -> bool: ...

    @overload
    def contains(
        self,
        item: TSource,
        /,
        *,
        comparer: Callable[[TSource, TSource], bool],
    ) -> bool: ...

    def contains(
        self,
        item: TSource,
        /,
        *,
        comparer: Callable[[TSource, TSource], bool] | None = None,
    ) -> bool: ...
