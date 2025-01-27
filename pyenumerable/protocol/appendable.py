from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .queryable import Queryable


class Appendable[TSource](Protocol):
    def append(self, item: TSource) -> "Queryable[TSource]": ...
