from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsSkip[TSource](Protocol):
    @overload
    def skip(self, count: int, /) -> "Enumerable[TSource]": ...

    @overload
    def skip(self, start: int, end: int, /) -> "Enumerable[TSource]": ...

    def skip_last(self, count: int, /) -> "Enumerable[TSource]": ...

    def skip_while(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> "Enumerable[TSource]": ...
