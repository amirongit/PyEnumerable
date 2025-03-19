from collections.abc import Callable
from typing import Protocol


class SupportsAverage[TSource](Protocol):
    def average(self, /) -> float: ...
