from collections.abc import Hashable

from . import (
    SupportsAggregation,
    SupportsAppend,
    SupportsAverage,
    SupportsChunk,
    SupportsCollectiveConditionCheck,
    SupportsConcatenation,
    SupportsCount,
    SupportsDistinction,
    SupportsExistenceCheck,
    SupportsGroup,
    SupportsGroupJoin,
    SupportsIndivisualConditionCheck,
    SupportsIntersection,
    SupportsJoin,
    SupportsMaximum,
    SupportsSubtraction,
    SupportsTransformation,
)


class Queryable[TSource: Hashable](
    SupportsAggregation[TSource],
    SupportsAppend[TSource],
    SupportsAverage[TSource],
    SupportsChunk[TSource],
    SupportsCollectiveConditionCheck[TSource],
    SupportsConcatenation[TSource],
    SupportsCount[TSource],
    SupportsDistinction[TSource],
    SupportsExistenceCheck[TSource],
    SupportsGroup[TSource],
    SupportsGroupJoin[TSource],
    SupportsIndivisualConditionCheck[TSource],
    SupportsIntersection[TSource],
    SupportsJoin[TSource],
    SupportsMaximum[TSource],
    SupportsSubtraction[TSource],
    SupportsTransformation[TSource],
): ...
