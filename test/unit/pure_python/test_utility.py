from __future__ import annotations

from dataclasses import dataclass
from random import choice


def generate_random_args(length: int, range_: range) -> tuple[int, ...]:
    """shouldn't be used inside test cases"""
    return tuple(choice(range_) for _ in range(length))


@dataclass(frozen=True, eq=True)
class Person:
    name: str
    age: int
    parent: Person | None = None


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int
