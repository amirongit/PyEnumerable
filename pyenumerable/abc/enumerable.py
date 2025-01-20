from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import (
    Callable,
    Collection,
    Hashable,
    Mapping,
    Sequence,
    Set,
)


class Enumerable[T: Hashable](ABC, Collection[T]):

    "corresponding to .NET 8"

    @abstractmethod
    def to_mapping[TK](self, func: Callable[[T], TK]) -> Mapping[TK, T]: ...

    @abstractmethod
    def to_set(self) -> Set[T]: ...

    @abstractmethod
    def aggregate[TA](
        self,
        func: Callable[[T, T], TA] | Callable[[TA, T], TA],
        seed: TA | None = None,
    ) -> TA: ...

    @abstractmethod
    def all(self, func: Callable[[T], bool]) -> bool: ...

    @abstractmethod
    def any(self, func: Callable[[T], bool] | None = None) -> bool: ...

    @abstractmethod
    def add(self, item: T) -> Enumerable[T]: ...

    @abstractmethod
    def average[TA: (int, float)](self, func: Callable[[T], TA]) -> TA: ...

    @abstractmethod
    def cast[TO](self, type_: type[TO]) -> Enumerable[TO]: ...

    @abstractmethod
    def chunk(self, size: int) -> Sequence[Enumerable[T]]: ...

    @abstractmethod
    def concat(self, other: Enumerable[T]) -> Enumerable[T]: ...

    @abstractmethod
    def contains(
        self,
        item: T,
        comparer: Callable[[T, T], bool] | None = None,
    ) -> bool: ...

    @abstractmethod
    def count(self, func: Callable[[T], bool] | None = None) -> int: ...

    @abstractmethod
    def distinct(
        self,
        comparer: Callable[[T, T], bool] | None = None,
    ) -> Enumerable[T]: ...
