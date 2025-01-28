from collections.abc import Hashable

from ._queryable import Queryable


class Associable[TKey: Hashable, TSource](Queryable[TSource]):
    @property
    def key(self) -> TKey: ...
