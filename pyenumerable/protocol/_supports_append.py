from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsAppend[TSource](Protocol):
    def append(self, element: TSource, /) -> "Enumerable[TSource]": ...
