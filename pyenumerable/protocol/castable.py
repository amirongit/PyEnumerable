from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyenumerable.abc.linq import LINQ


class Castable[TSource](Protocol):
    def cast[TResult](self, type_: type[TResult]) -> "LINQ[TResult]": ...
