import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person, Point


class TestOrderMethod:
    def test_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.order()

        assert res.source == ()

    def test_exc_raise_when_uncomparable(self) -> None:
        obj = PurePythonEnumerable(
            Person("jane doe", 28, Person("james doe", 32)),
            Person("john doe", 19),
        )

        with pytest.raises(TypeError):
            obj.order()

    def test_without_comparer(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(7))))

        res = obj.order()

        assert res.source == tuple(sorted(items))

    def test_with_comparer(self) -> None:
        obj = PurePythonEnumerable(
            fifth := Point(0, 5),
            second := Point(0, 2),
            fourth := Point(0, 4),
            first := Point(0, 1),
            third := Point(0, 3),
        )

        res = obj.order(
            comparer=lambda first_point, second_point: first_point.y
            < second_point.y
        )

        assert res.source == (first, second, third, fourth, fifth)
