from collections.abc import Collection
from typing import Protocol

from . import (
    SupportsAggregate,
    SupportsAll,
    SupportsAny,
    SupportsAppend,
    SupportsAverage,
    SupportsChunk,
    SupportsConcat,
    SupportsContains,
    SupportsCount,
    SupportsDistinct,
    SupportsExcept,
    SupportsGroupBy,
    SupportsGroupJoin,
    SupportsIntersect,
    SupportsJoin,
    SupportsMax,
    SupportsMin,
    SupportsOfType,
    SupportsOrder,
    SupportsPrepend,
    SupportsReverse,
    SupportsSelect,
    SupportsSequenceEqual,
    SupportsSingle,
    SupportsSkip,
    SupportsSum,
    SupportsTake,
    SupportsUnion,
    SupportsWhere,
    SupportsZip,
)


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
    def source(self) -> Collection[TSource]: ...
