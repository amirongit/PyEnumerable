from collections.abc import Callable
from random import choice

from pyenumerable.implementations.pure_python import Enumerable
from test.unit.pure_python.test_utility import generate_random_args


class TestSelectMethod:
    def test_with_index(self) -> None:
        obj = Enumerable(
            *generate_random_args(choice(range(100)), range(-25, 25)),
        )

        res = obj.select(TestSelectMethod.combine_index_and_value)

        assert res.source == tuple(
            TestSelectMethod.combine_index_and_value(i, v) for i,
            v in enumerate(obj.source)
        )

    def test_without_index(self) -> None:
        obj = Enumerable(
            *generate_random_args(choice(range(100)), range(-25, 25)),
        )

        res = obj.select(TestSelectMethod.raise_to_the_power_of_two)

        assert res.source == tuple(
            TestSelectMethod.raise_to_the_power_of_two(i, v) for i,
            v in enumerate(obj.source)
        )

    @staticmethod
    def combine_index_and_value(index: int, value: int) -> str:
        return f"{index}: {value}"

    @staticmethod
    def raise_to_the_power_of_two(_: int, value: int) -> int:
        return value ** 2
