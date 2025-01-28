from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsConcatenation[TSource](Protocol):
    def concat(
        self,
        other: "Queryable[TSource]",
        /,
    ) -> "Queryable[TSource]": ...
