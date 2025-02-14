from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from _queryable import Queryable


class SupportsSelect[TSource](Protocol):
    def select[TResult](
        self,
        selector: Callable[[int, TSource], TResult],
    ) -> "Queryable[TResult]": ...
