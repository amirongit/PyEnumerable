from collections.abc import Hashable

from . import (
    Aggregable,
    Appendable,
    Averageable,
    Castable,
    Checkable,
    Chunkable,
    Concatable,
    Countable,
    Dividable,
    Fillable,
    Groupable,
    GroupJoinable,
    Intersectable,
    Joinable,
    Pickable,
    Subtractable,
)


class Queryable[TSource: Hashable](
    Aggregable[TSource],
    Appendable[TSource],
    Averageable[TSource],
    Castable[TSource],
    Checkable[TSource],
    Chunkable[TSource],
    Concatable[TSource],
    Countable[TSource],
    Dividable[TSource],
    Fillable[TSource],
    Groupable[TSource],
    GroupJoinable[TSource],
    Intersectable[TSource],
    Joinable[TSource],
    Pickable[TSource],
    Subtractable[TSource],
): ...
