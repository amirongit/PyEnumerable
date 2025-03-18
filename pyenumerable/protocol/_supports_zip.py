from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsZip[TSource](Protocol):
    def zip[TSecond](
        self,
        second: "Enumerable[TSecond]",
        /,
    ) -> "Enumerable[tuple[TSource, TSecond]]": ...
