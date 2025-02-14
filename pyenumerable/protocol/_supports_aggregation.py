from collections.abc import Callable
from typing import Protocol, overload


class SupportsAggregation[TSource](Protocol):
    @overload
    def aggregate[TAccumulate](
        self,
        func: Callable[[TSource, TSource], TAccumulate],
        /,
    ) -> TAccumulate: ...

    @overload
    def aggregate[TAccumulate](
        self,
        func: Callable[[TAccumulate, TSource], TAccumulate],
        /,
        *,
        seed: TAccumulate,
    ) -> TAccumulate: ...
