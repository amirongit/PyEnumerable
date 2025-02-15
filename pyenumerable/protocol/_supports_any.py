from collections.abc import Callable
from typing import Protocol, overload


class SupportsAny[TSource](Protocol):
    @overload
    def any(self, /) -> bool: ...

    @overload
    def any(self, predicate: Callable[[TSource], bool], /) -> bool: ...
