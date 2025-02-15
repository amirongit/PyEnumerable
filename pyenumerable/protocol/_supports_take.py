from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsTake[TSource](Protocol):
    @overload
    def take(self, count: int, /) -> "Queryable[TSource]": ...

    @overload
    def take(self, start: int, end: int, /) -> "Queryable[TSource]": ...

    def take_last(self, count: int, /) -> "Queryable[TSource]": ...

    def take_while(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> "Queryable[TSource]": ...
