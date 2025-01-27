from collections.abc import Hashable, Sequence

from pyenumerable.protocol import Queryable


class LINQ[TSource: Hashable](Sequence[TSource], Queryable[TSource]): ...
