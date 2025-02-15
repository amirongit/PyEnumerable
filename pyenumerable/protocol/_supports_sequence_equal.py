from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._enumerable import Enumerable


class SupportsSequenceEqual[TSource](Protocol):
    @overload
    def sequence_equal(self, other: "Enumerable[TSource]", /) -> bool: ...

    @overload
    def sequence_equal(
        self,
        other: "Enumerable[TSource]",
        /,
        *,
        comparer: Comparer[TSource],
    ) -> bool: ...
