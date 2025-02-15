from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._queryable import Queryable


class SupportsSequenceEqual[TSource](Protocol):
    @overload
    def sequence_equal(self, other: "Queryable[TSource]", /) -> bool: ...

    @overload
    def sequence_equal(
        self,
        other: "Queryable[TSource]",
        /,
        *,
        comparer: Comparer[TSource],
    ) -> bool: ...
