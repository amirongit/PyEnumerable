from random import choice

from pyenumerable.implementations.pure_python import Enumerable
from test.unit.pure_python.test_utility import generate_random_args


class TestEnumerableConstructor:
    def test_initialization_with_raw_items(self) -> None:
        args = generate_random_args(choice(range(100)), range(-25, 25))
        obj = Enumerable(*args)

        assert args == obj.source

    def test_initialization_with_packed_items(self) -> None:
        first_pack = generate_random_args(choice(range(10)), range(-25, 25))
        second_pack = generate_random_args(choice(range(10)), range(-25, 25))
        obj = Enumerable(from_iterables=((first_pack, second_pack)))

        assert first_pack + second_pack == obj.source

    def test_initialization_with_raw_and_packed_items(self) -> None:
        raw_items = generate_random_args(choice(range(10)), range(-25, 25))
        second_pack = generate_random_args(choice(range(10)), range(-25, 25))
        obj = Enumerable(*raw_items, from_iterables=(second_pack,))

        assert raw_items + second_pack == obj.source
