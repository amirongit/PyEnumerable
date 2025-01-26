from collections.abc import Callable
from typing import Protocol, overload


class Averageable[TSource](Protocol):
    @overload
    def average[TAccumulate: int](
        self,
        func: Callable[[TSource], TAccumulate],
    ) -> TAccumulate: ...

    @overload
    def average[TAccumulate: int](
        self,
        func: Callable[[TSource], TAccumulate | None],
    ) -> TAccumulate: ...

    @overload
    def average[TAccumulate: float](
        self,
        func: Callable[[TSource], TAccumulate],
    ) -> TAccumulate: ...

    @overload
    def average[TAccumulate: float](
        self,
        func: Callable[[TSource], TAccumulate | None],
    ) -> TAccumulate: ...

    def average[TAccumulate: (float, int)](
        self,
        func: Callable[[TSource], TAccumulate | None],
    ) -> TAccumulate: ...
