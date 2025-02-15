from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsConcat[TSource](Protocol):
    def concat(
        self,
        other: "Enumerable[TSource]",
        /,
    ) -> "Enumerable[TSource]": ...
