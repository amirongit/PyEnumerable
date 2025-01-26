from typing import Protocol

from pyenumerable.protocol.enumerable import Enumerable


class Appendable[TSource](Protocol):
    def append(self, item: TSource) -> Enumerable[TSource]: ...
