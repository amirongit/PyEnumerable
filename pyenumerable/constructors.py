from collections.abc import Iterable

from pyenumerable.implementations import PurePythonEnumerable
from pyenumerable.protocol import Enumerable


def pp_enumerable[TSource](
    *items: TSource, from_iterable: Iterable[Iterable[TSource]] | None = None
) -> Enumerable[TSource]:
    return PurePythonEnumerable(*items, from_iterable=from_iterable)
