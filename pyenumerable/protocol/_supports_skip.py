from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsSkip[TSource](Protocol):
    @overload
    def skip(self, count: int, /) -> "Queryable[TSource]": ...

    @overload
    def skip(self, start: int, end: int, /) -> "Queryable[TSource]": ...

    def skip_last(self, count: int, /) -> "Queryable[TSource]": ...

    def skip_while(
        self,
        count: int,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> "Queryable[TSource]": ...
