from typing import Protocol


class SupportsSum[TSource](Protocol):
    def sum(self, /) -> TSource: ...
