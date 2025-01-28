from collections.abc import Callable
from typing import Protocol, overload


class SupportsAverage[TSource](Protocol):
    @overload
    def average[TAccumulate: int](
        self,
        selector: Callable[[TSource], TAccumulate],
        /,
    ) -> TAccumulate: ...

    @overload
    def average[TAccumulate: int](
        self,
        selector: Callable[[TSource], TAccumulate | None],
        /,
    ) -> TAccumulate: ...

    @overload
    def average[TAccumulate: float](
        self,
        selector: Callable[[TSource], TAccumulate],
        /,
    ) -> TAccumulate: ...

    @overload
    def average[TAccumulate: float](
        self,
        selector: Callable[[TSource], TAccumulate | None],
        /,
    ) -> TAccumulate: ...

    def average[TAccumulate: (float, int)](
        self,
        selector: Callable[[TSource], TAccumulate | None],
        /,
    ) -> TAccumulate: ...
