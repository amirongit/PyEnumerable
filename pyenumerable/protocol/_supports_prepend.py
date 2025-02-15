from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsPrepend[TSource](Protocol):
    def prepend(self, item: TSource, /) -> "Enumerable[TSource]": ...
