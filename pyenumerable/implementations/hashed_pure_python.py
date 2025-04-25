from collections.abc import Hashable

from pyenumerable.implementations.pure_python import PurePythonEnumerable


class HashedPurePythonEnumerable[TSource: Hashable](
    PurePythonEnumerable[TSource]
): ...
