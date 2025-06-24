from collections.abc import Callable
from typing import Protocol, overload


class SupportsAny[TSource](Protocol):
    @overload
    def any_(self, /) -> bool: ...

    @overload
    def any_(self, predicate: Callable[[TSource], bool], /) -> bool: ...
