import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestUnionMethod:
    def test_exc_raise_when_unhashable(self) -> None:
        first_object = PurePythonEnumerable(Point(0, 1), Point(1, 0))
        second_object = PurePythonEnumerable(Point(1, 0), Point(0, 1))

        with pytest.raises(TypeError):
            first_object.union(second_object)

    def test_union(self) -> None:
        first_object = PurePythonEnumerable(*(items := tuple(range(7))))
        second_object = PurePythonEnumerable(*(-i for i in items))

        res = first_object.union(
            second_object, comparer=lambda x, y: abs(x) == abs(y)
        )

        assert res.source == items

    def test_overlap_remove_for_self(self) -> None:
        first_object = PurePythonEnumerable(first := Point(0, 1), Point(1, 1))
        second_object = PurePythonEnumerable(
            second := Point(2, 3), third := Point(4, 5)
        )

        res = first_object.union(
            second_object,
            comparer=lambda first_point, second_point: first_point.y
            == second_point.y,
        )

        assert res.source == (first, second, third)

    def test_overlap_remove_for_second(self) -> None:
        first_object = PurePythonEnumerable(
            first := Point(2, 3), second := Point(4, 5)
        )
        second_object = PurePythonEnumerable(third := Point(0, 1), Point(1, 1))

        res = first_object.union(
            second_object,
            comparer=lambda first_point, second_point: first_point.y
            == second_point.y,
        )

        assert res.source == (first, second, third)
