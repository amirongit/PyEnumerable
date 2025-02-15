from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsZip[TSource](Protocol):
    @overload
    def zip[TSecond](
        self,
        second: TSecond,
        /,
    ) -> "Enumerable[tuple[TSource, TSecond]]": ...

    @overload
    def zip[TSecond, TResult](
        self,
        second: TSecond,
        result_selector: Callable[[TSource, TSecond], TResult],
        /,
    ) -> "Enumerable[TResult]": ...
