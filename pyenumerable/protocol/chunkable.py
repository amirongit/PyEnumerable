from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .queryable import Queryable


class Chunkable[TSource](Protocol):
    def chunk(self, size: int) -> Sequence["Queryable[TSource]"]: ...
