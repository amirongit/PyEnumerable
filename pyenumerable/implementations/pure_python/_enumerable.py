from collections.abc import Iterable


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
