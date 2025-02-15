from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsWhere[TSource](Protocol):
    def where(
        self,
        predicate: Callable[[int, TSource], bool],
        /,
    ) -> "Enumerable[TSource]": ...
