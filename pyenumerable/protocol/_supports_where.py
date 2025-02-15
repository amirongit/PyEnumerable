from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsWhere[TSource](Protocol):
    def where(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> "Queryable[TSource]": ...
