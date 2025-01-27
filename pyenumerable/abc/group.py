from abc import ABC, abstractmethod
from collections.abc import Hashable

from pyenumerable.protocol import Queryable


class Group[TKey: Hashable, TSource](ABC, Hashable, Queryable[TSource]):
    @property
    @abstractmethod
    def key(self) -> TKey: ...
