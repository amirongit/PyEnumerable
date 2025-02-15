from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsReverse[TSource](Protocol):
    def reverse(self, /) -> "Enumerable[TSource]": ...
