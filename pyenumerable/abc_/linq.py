from collections.abc import Sequence

from pyenumerable.protocol import Queryable


class LINQ[TSource](Sequence[TSource], Queryable[TSource]): ...
