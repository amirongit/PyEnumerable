from collections.abc import Callable
from typing import Protocol, overload


class Pickable[TSource](Protocol):
    @overload
    def any(self) -> bool: ...

    @overload
    def any(self, func: Callable[[TSource], bool]) -> bool: ...

    def any(self, func: Callable[[TSource], bool] | None = None) -> bool: ...
