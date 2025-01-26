from typing import Protocol

from pyenumerable.abc.enumerable import Enumerable


class Concatable[TSource](Protocol):
    def concat(self, other: Enumerable[TSource]) -> Enumerable[TSource]: ...
