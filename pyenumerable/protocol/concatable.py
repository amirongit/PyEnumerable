from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyenumerable.abc.enumerable import Enumerable


class Concatable[TSource](Protocol):
    def concat(
        self,
        other: "Enumerable[TSource]",
    ) -> "Enumerable[TSource]": ...
