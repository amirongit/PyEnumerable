from collections.abc import Callable
from typing import Protocol


class SupportsCollectiveConditionCheck[TSource](Protocol):
    def all(self, predicate: Callable[[TSource], bool], /) -> bool: ...
