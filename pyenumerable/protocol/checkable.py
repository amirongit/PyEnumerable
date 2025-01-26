from collections.abc import Callable
from typing import Protocol


class Checkable[TSource](Protocol):
    def all(self, func: Callable[[TSource], bool]) -> bool: ...
