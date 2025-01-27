from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyenumerable.abc.linq import LINQ


class Concatable[TSource](Protocol):
    def concat(self, other: "LINQ[TSource]") -> "LINQ[TSource]": ...
