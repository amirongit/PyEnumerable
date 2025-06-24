from typing import Any

from pyenumerable.protocol._enumerable import Enumerable


def assume_not_empty(instance: Enumerable[Any]) -> None:
    if instance.count_() == 0:
        msg = "Enumerable is empty"
        raise ValueError(msg)
