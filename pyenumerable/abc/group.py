from collections.abc import Hashable, Sequence

from pyenumerable.protocol import Associable


class Group[TKey, TSource](
    Hashable,
    Sequence[TSource],
    Associable[TKey, TSource],
): ...
