from ._enumerable import Enumerable


class Associable[TKey, TSource](Enumerable[TSource]):
    @property
    def key(self) -> TKey: ...
