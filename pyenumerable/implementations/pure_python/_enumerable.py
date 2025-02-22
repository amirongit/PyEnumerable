from __future__ import annotations

from collections.abc import Callable, Iterable
from itertools import chain
from typing import Protocol, cast


class PurePythonEnumerable[TSource]:

    # TODO
    # change return types to pyenumerable.protocol.Enumerable

    def __init__(
        self,
        *items: TSource,
        from_iterables: Iterable[Iterable[TSource]] | None = None,
    ) -> None:
        self._source: tuple[TSource, ...] = items

        if from_iterables is not None:
            self._source += tuple(chain(*from_iterables))

    @property
    def source(self) -> tuple[TSource, ...]:
        return self._source

    def select[TResult](
        self,
        selector: Callable[[int, TSource], TResult],
        /,
    ) -> PurePythonEnumerable[TResult]:
        return PurePythonEnumerable(
            *tuple(selector(i, v) for i, v in enumerate(self.source)),
       )

    def select_many[TResult](
        self,
        selector: Callable[[int, TSource], Iterable[TResult]],
        /,
    ) -> PurePythonEnumerable[TResult]:
        return PurePythonEnumerable(
            from_iterables=[selector(i, v) for i, v in enumerate(self.source)],
        )
