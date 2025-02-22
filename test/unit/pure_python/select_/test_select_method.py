from collections.abc import Callable
from random import choice

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import generate_random_args


class TestSelectMethod:
    def test_functionality(self) -> None:
        obj = PurePythonEnumerable(
            *(
                items := generate_random_args(
                    choice(range(100)),
                    range(-25, 25),
                )
            ),
        )

        res = obj.select(TestSelectMethod.combine_index_and_value)

        assert res.source == tuple(
            TestSelectMethod.combine_index_and_value(i, v) for i,
            v in enumerate(items)
        )

    @staticmethod
    def combine_index_and_value(index: int, value: int) -> str:
        return f"{index}: {value}"
