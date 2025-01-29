from ._queryable import Queryable


class Associable[TKey, TSource](Queryable[TSource]):
    @property
    def key(self) -> TKey: ...
