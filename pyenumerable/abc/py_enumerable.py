from abc import ABC, abstractmethod
from collections.abc import Callable, Collection, Mapping, Set


class PyEnumerable[T](ABC, Collection[T]):

    @abstractmethod
    def to_mapping[TK](
        self,
        key_selector: Callable[[T], TK],
    ) -> Mapping[TK, T]: ...

    @abstractmethod
    def to_set(self) -> Set[T]: ...

    @abstractmethod
    def aggregate[TA](self, accumulator: Callable[[T, T], TA]) -> TA: ...

    @abstractmethod
    def aggregate_with_seed[TA](
        self,
        seed: TA,
        accumulator: Callable[[TA, T], TA],
    ) -> TA: ...

    @abstractmethod
    def aggregate_with_seed_and_selector[TA, TS](
        self,
        seed: TA,
        accumulator: Callable[[TA, T], TA],
        selector: Callable[[TA], TS],
    ) -> TS: ...

