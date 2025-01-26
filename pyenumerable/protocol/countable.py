from collections.abc import Callable
from typing import Protocol, overload


class Countable[TSource](Protocol):
    @overload
    def count_(self) -> int: ...

    @overload
    def count_(self, func: Callable[[TSource], bool]) -> int: ...

    def count_(self, func: Callable[[TSource], bool] | None = None) -> int: ...
