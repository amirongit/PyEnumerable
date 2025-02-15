from collections.abc import Callable
from typing import Protocol, overload

from pyenumerable.typing_utility import Addable


class SupportsSum[TSource](Protocol):
    @overload
    def sum(self, /) -> TSource: ...

    @overload
    def sum[TItem: Addable](
        self,
        selector: Callable[[TSource], TItem],
        /,
    ) -> TItem: ...
