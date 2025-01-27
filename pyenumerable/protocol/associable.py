from collections.abc import Hashable
from typing import TYPE_CHECKING

from .queryable import Queryable


class Associable[TKey: Hashable, TSource](Queryable[TSource]):
    @property
    def key(self) -> TKey: ...
