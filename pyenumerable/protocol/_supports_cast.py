from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsCast[TSource](Protocol):
    def cast[TResult](
        self,
        type_: type[TResult],
        /,
    ) -> "Enumerable[TResult]": ...
