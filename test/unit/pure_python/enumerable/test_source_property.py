from random import choice

from pyenumerable.implementations.pure_python import Enumerable


class TestEnumerableConstructor:
    def test_initialization_with_raw_items(self) -> None:
        args = TestEnumerableConstructor.generate_random_args(
            choice(range(100)),
            range(-25, 25),
        )

        enum = Enumerable(*args)

        assert args == enum.source

    def test_initialization_with_packed_items(self) -> None:
        first_pack = TestEnumerableConstructor.generate_random_args(
            choice(range(10)),
            range(-25, 25),
        )

        second_pack = TestEnumerableConstructor.generate_random_args(
            choice(range(10)),
            range(-25, 25),
        )

        enum = Enumerable(from_iterables=((first_pack, second_pack)))

        assert first_pack + second_pack == enum.source

    def test_initialization_with_raw_and_packed_items(self) -> None:
        raw_items = TestEnumerableConstructor.generate_random_args(
            choice(range(10)),
            range(-25, 25),
        )

        second_pack = TestEnumerableConstructor.generate_random_args(
            choice(range(10)),
            range(-25, 25),
        )

        enum = Enumerable(*raw_items, from_iterables=(second_pack,))

        assert raw_items + second_pack == enum.source

    @staticmethod
    def generate_random_args(length: int, range_: range) -> tuple[int, ...]:
        return tuple(choice(range_) for _ in range(length))

