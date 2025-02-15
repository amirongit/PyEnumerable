from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsTypeOf[TSource](Protocol):
    def of_type[TResult](
        self,
        type_: type[TResult],
        /,
    ) -> "Enumerable[TResult]": ...
