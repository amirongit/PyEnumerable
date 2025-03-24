from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, overload

from pyenumerable.typing_utility import Comparer

if TYPE_CHECKING:
    from ._associable import Associable
    from ._enumerable import Enumerable


class SupportsGroupBy[TSource](Protocol):
    @overload
    def group_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
    ) -> "Enumerable[Associable[TKey, TSource]]": ...

    @overload
    def group_by[TKey](
        self,
        key_selector: Callable[[TSource], TKey],
        /,
        *,
        comparer: Comparer[TKey],
    ) -> "Enumerable[Associable[TKey, TSource]]": ...
