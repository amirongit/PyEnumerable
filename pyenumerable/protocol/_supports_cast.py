from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsCast[TSource](Protocol):
    def cast[TResult](
        self,
        type_: type[TResult],
        /,
    ) -> "Queryable[TResult]": ...
