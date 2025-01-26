from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyenumerable.abc.enumerable import Enumerable


class Chunkable[TSource](Protocol):
    def chunk(self, size: int) -> Sequence["Enumerable[TSource]"]: ...
