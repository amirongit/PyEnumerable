from collections.abc import Callable
from typing import Protocol, overload


class Aggregable[TSource](Protocol):
    @overload
    def aggregate[TAccumulate](
        self,
        func: Callable[[TSource, TSource], TAccumulate],
    ) -> TAccumulate: ...

    @overload
    def aggregate[TAccumulate](
        self,
        func: Callable[[TAccumulate, TSource], TAccumulate],
        seed: TAccumulate,
    ) -> TAccumulate: ...

    def aggregate[TAccumulate](
        self,
        func: Callable[
            [TSource, TSource],
            TAccumulate,
        ] | Callable[
            [TAccumulate, TSource],
            TAccumulate,
        ],
        seed: TAccumulate | None = None,
    ) -> TAccumulate: ...
