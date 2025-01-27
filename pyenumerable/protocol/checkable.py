from collections.abc import Callable
from typing import Protocol


class Checkable[TSource](Protocol):
    def all(self, predicate: Callable[[TSource], bool], /) -> bool: ...
