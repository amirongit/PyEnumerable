from collections.abc import Callable, Hashable, Mapping, Set
from typing import Protocol


# TODO
# inherit from suitable abc.collections
# make sure to support ordering
class Enumerable[TSource: Hashable](Protocol):
    ...
