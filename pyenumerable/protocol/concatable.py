from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .queryable import Queryable


class Concatable[TSource](Protocol):
    def concat(self, other: "Queryable[TSource]") -> "Queryable[TSource]": ...
