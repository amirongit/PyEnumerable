from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsPrepend[TSource](Protocol):
    def prepend(self, item: TSource, /) -> "Queryable[TSource]": ...
