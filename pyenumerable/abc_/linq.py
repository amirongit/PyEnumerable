from collections.abc import Sequence

from pyenumerable.protocol import Enumerable


class LINQ[TSource](Sequence[TSource], Enumerable[TSource]): ...
