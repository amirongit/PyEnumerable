from collections.abc import Callable
from typing import Protocol, overload


class SupportsIndivisualConditionCheck[TSource](Protocol):
    @overload
    def any(self, /) -> bool: ...

    @overload
    def any(self, predicate: Callable[[TSource], bool], /) -> bool: ...
