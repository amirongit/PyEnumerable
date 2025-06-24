from typing import Protocol


class SupportsSum[TSource](Protocol):
    def sum_(self, /) -> TSource: ...
