from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsChunk[TSource](Protocol):
    def chunk(self, size: int, /) -> tuple["Enumerable[TSource]", ...]: ...
