from typing import Protocol

from pyenumerable.abc.enumerable import Enumerable


class Castable[TSource](Protocol):
    def cast[TResult](self, type_: type[TResult]) -> Enumerable[TResult]: ...
