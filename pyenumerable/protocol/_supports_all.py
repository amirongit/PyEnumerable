from collections.abc import Callable
from typing import Protocol


class SupportsAll[TSource](Protocol):
    def all(self, predicate: Callable[[TSource], bool], /) -> bool: ...
