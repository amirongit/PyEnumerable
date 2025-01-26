from __future__ import annotations

from collections.abc import Hashable, Sequence

from pyenumerable.protocol import (
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


class Enumerable[TSource: Hashable](
    Sequence[TSource],
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
