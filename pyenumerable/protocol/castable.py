from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .queryable import Queryable


class Castable[TSource](Protocol):
    def cast[TResult](
        self,
        type_: type[TResult],
        /,
    ) -> "Queryable[TResult]": ...
