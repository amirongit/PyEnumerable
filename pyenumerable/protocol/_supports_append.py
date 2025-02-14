from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsAppend[TSource](Protocol):
    def append(self, item: TSource, /) -> "Queryable[TSource]": ...
