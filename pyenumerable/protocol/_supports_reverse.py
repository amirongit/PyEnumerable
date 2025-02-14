from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsReverse[TSource](Protocol):
    def reverse(self) -> "Queryable[TSource]": ...
