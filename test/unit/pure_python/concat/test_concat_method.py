from random import choice

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import generate_random_args


class TestConcatMethod:
    def test_functionality(self) -> None:
        first = PurePythonEnumerable(
            *(
                first_items := generate_random_args(
                    choice(range(100)),
                    range(-25, 25),
                )
            ),
        )

        second = PurePythonEnumerable(
            *(
                second_items := generate_random_args(
                    choice(range(100)),
                    range(-25, 25),
                )
            ),
        )

        final = first.concat(second)

        assert final.source == first_items + second_items
