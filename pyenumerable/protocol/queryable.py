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
    Differentiable,
    Dividable,
    Fillable,
    Pickable,
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
    Differentiable[TSource],
    Dividable[TSource],
    Fillable[TSource],
    Pickable[TSource],
): ...
