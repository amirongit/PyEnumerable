from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyenumerable.abc.enumerable import Enumerable


class Castable[TSource](Protocol):
    def cast[TResult](self, type_: type[TResult]) -> "Enumerable[TResult]": ...
