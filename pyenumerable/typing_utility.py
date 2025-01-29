from collections.abc import Callable

type Comparer[T] = Callable[[T,T], bool]
