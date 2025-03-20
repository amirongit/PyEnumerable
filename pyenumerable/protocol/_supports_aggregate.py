from collections.abc import Callable
from typing import Protocol, overload


class SupportsAggregate[TSource](Protocol):
    @overload
    def aggregate(
        self,
        func: Callable[[TSource, TSource], TSource],
        /,
    ) -> TSource: ...

    @overload
    def aggregate(
        self, func: Callable[[TSource, TSource], TSource], /, *, seed: TSource
    ) -> TSource: ...
