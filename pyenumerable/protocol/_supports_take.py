from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsTake[TSource](Protocol):
    @overload
    def take(self, count: int, /) -> "Enumerable[TSource]": ...

    @overload
    def take(self, start: int, end: int, /) -> "Enumerable[TSource]": ...

    def take_last(self, count: int, /) -> "Enumerable[TSource]": ...

    def take_while(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> "Enumerable[TSource]": ...
