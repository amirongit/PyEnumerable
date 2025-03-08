from __future__ import annotations

from dataclasses import dataclass
from random import choice


def generate_random_args(length: int, range_: range) -> tuple[int, ...]:
    return tuple(choice(range_) for _ in range(length))


@dataclass
class Person:
    name: str
    age: int
    parent: Person | None = None


@dataclass
class Point:
    x: int
    y: int
