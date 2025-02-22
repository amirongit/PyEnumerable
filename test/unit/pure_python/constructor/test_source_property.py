from random import choice

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import generate_random_args


class TestEnumerableConstructor:
    def test_initialization_with_raw_items(self) -> None:
        obj = PurePythonEnumerable(
            *(
                items := generate_random_args(
                    choice(range(100)),
                    range(-25, 25),
                )
            ),
        )

        assert items == obj.source

    def test_initialization_with_packed_items(self) -> None:
        obj = PurePythonEnumerable(
            from_iterables=(
                (
                    first := generate_random_args(
                        choice(range(10)),
                        range(-25, 25),
                    ),
                    second := generate_random_args(
                        choice(range(10)),
                        range(-25, 25),
                    ),
                )
            ),
        )

        assert first + second == obj.source

    def test_initialization_with_raw_and_packed_items(self) -> None:
        obj = PurePythonEnumerable(
            *(
                raw := generate_random_args(
                    choice(range(10)),
                    range(-25, 25),
                )
            ),
            from_iterables=(
                packed := generate_random_args(
                    choice(range(10)),
                    range(-25, 25),
                ),
            ),
        )

        assert raw + packed == obj.source
