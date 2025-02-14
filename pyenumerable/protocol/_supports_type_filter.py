from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsTypeFilter[TSource](Protocol):
    def of_type[TResult](
        self,
        type_: type[TResult],
        /,
    ) -> "Queryable[TResult]": ...
