from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsChunk[TSource](Protocol):
    def chunk(self, size: int, /) -> Sequence["Queryable[TSource]"]: ...
