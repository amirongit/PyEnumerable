from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyenumerable.abc.linq import LINQ


class Chunkable[TSource](Protocol):
    def chunk(self, size: int) -> Sequence["LINQ[TSource]"]: ...
