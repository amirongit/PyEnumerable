from collections.abc import Callable
from typing import Protocol, overload


class Countable[TSource](Protocol):
    @overload
    def count(self) -> int: ...

    @overload
    def count(self, func: Callable[[TSource], bool]) -> int: ...

    def count(self, func: Callable[[TSource], bool] | None = None) -> int: ...
