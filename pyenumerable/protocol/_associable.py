from typing import Protocol

from ._enumerable import Enumerable


class Associable[TKey, TSource](Enumerable[TSource], Protocol):
    @property
    def key(self) -> TKey: ...
