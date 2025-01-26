from collections.abc import Sequence
from typing import Protocol

from pyenumerable.abc.enumerable import Enumerable


class Chunkable[TSource](Protocol):
    def chunk(self, size: int) -> Sequence[Enumerable[TSource]]: ...
