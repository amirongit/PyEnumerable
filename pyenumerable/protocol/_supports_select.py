from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsSelect[TSource](Protocol):
    def select[TResult](
        self,
        selector: Callable[[int, TSource], TResult],
        /,
    ) -> "Enumerable[TResult]": ...

    def select_many[TResult](
        self,
        selector: Callable[[int, TSource], Iterable[TResult]],
        /,
    ) -> "Enumerable[TResult]": ...
