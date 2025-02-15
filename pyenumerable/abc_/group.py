from collections.abc import Sequence

from pyenumerable.protocol import Associable


class Group[TKey, TSource](
    Sequence[TSource],
    Associable[TKey, TSource],
): ...
