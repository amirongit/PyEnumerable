from __future__ import annotations

from dataclasses import dataclass
from random import choice


@dataclass(frozen=True, eq=True)
class Person:
    name: str
    age: int
    parent: Person | None = None


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int
