from __future__ import annotations

from collections.abc import Callable, Iterable


class Enumerable[TSource]:
    def __init__(
        self,
        *items: TSource,
        from_iterables: Iterable[Iterable[TSource]] | None = None,
    ) -> None:
        self._source: tuple[TSource, ...] = items

        if from_iterables is not None:
            for iterable in from_iterables:
                self._source += tuple(iterable)

    @property
    def source(self) -> tuple[TSource, ...]:
        return self._source

    def select[TResult](
        self,
        selector: Callable[[int, TSource], TResult],
        /,
    ) -> Enumerable[TResult]:
        return Enumerable(
            *tuple(selector(i, v) for i, v in enumerate(self.source)),
        )
