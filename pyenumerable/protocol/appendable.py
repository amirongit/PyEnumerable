from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyenumerable.abc.linq import LINQ


class Appendable[TSource](Protocol):
    def append(self, item: TSource) -> "LINQ[TSource]": ...
