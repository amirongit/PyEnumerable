from collections.abc import Callable
from typing import Protocol, overload

from pyenumerable.typing_utility import Comparer


class SupportsContains[TSource](Protocol):
    @overload
    def contains(
        self,
        item: TSource,
        /,
    ) -> bool: ...

    @overload
    def contains(
        self,
        item: TSource,
        /,
        *,
        comparer: Comparer[TSource],
    ) -> bool: ...
