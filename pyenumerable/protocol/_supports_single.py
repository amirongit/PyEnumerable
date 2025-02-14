from collections.abc import Callable
from typing import Protocol, overload


class SupportsSingle[TSource](Protocol):
    @overload
    def single(self, /) -> TSource: ...

    @overload
    def single(self, predicate: Callable[[TSource], bool], /) -> TSource: ...

    @overload
    def single_or_deafult(self, default: TSource, /) -> TSource: ...

    @overload
    def single_or_deafult(
        self,
        default: TSource,
        predicate: Callable[[TSource], bool],
        /,
    ) -> TSource: ...
