from typing import Protocol

from ._supports_aggregate import SupportsAggregate
from ._supports_all import SupportsAll
from ._supports_any import SupportsAny
from ._supports_append import SupportsAppend
from ._supports_average import SupportsAverage
from ._supports_chunk import SupportsChunk
from ._supports_concat import SupportsConcat
from ._supports_contains import SupportsContains
from ._supports_count import SupportsCount
from ._supports_distinct import SupportsDistinct
from ._supports_except import SupportsExcept
from ._supports_group_by import SupportsGroupBy
from ._supports_group_join import SupportsGroupJoin
from ._supports_intersect import SupportsIntersect
from ._supports_join import SupportsJoin
from ._supports_max import SupportsMax
from ._supports_min import SupportsMin
from ._supports_of_type import SupportsOfType
from ._supports_order import SupportsOrder
from ._supports_prepend import SupportsPrepend
from ._supports_reverse import SupportsReverse
from ._supports_select import SupportsSelect
from ._supports_sequence_equal import SupportsSequenceEqual
from ._supports_single import SupportsSingle
from ._supports_skip import SupportsSkip
from ._supports_sum import SupportsSum
from ._supports_take import SupportsTake
from ._supports_union import SupportsUnion
from ._supports_where import SupportsWhere
from ._supports_zip import SupportsZip


class Enumerable[TSource](
    SupportsAggregate[TSource],
    SupportsAll[TSource],
    SupportsAny[TSource],
    SupportsAppend[TSource],
    SupportsAverage[TSource],
    SupportsChunk[TSource],
    SupportsConcat[TSource],
    SupportsContains[TSource],
    SupportsCount[TSource],
    SupportsDistinct[TSource],
    SupportsExcept[TSource],
    SupportsGroupBy[TSource],
    SupportsGroupJoin[TSource],
    SupportsIntersect[TSource],
    SupportsJoin[TSource],
    SupportsMax[TSource],
    SupportsMin[TSource],
    SupportsOfType[TSource],
    SupportsOrder[TSource],
    SupportsPrepend[TSource],
    SupportsReverse[TSource],
    SupportsSelect[TSource],
    SupportsSequenceEqual[TSource],
    SupportsSingle[TSource],
    SupportsSkip[TSource],
    SupportsSum[TSource],
    SupportsTake[TSource],
    SupportsUnion[TSource],
    SupportsWhere[TSource],
    SupportsZip[TSource],
    Protocol,
):
    @property
    def source(self) -> tuple[TSource, ...]: ...

    def __str__(self) -> str:
        return f"Enumerable(*{self.source})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(*{self.source})"
