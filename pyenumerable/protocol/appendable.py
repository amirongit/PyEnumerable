from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyenumerable.abc.enumerable import Enumerable


class Appendable[TSource](Protocol):
    def append(self, item: TSource) -> "Enumerable[TSource]": ...
