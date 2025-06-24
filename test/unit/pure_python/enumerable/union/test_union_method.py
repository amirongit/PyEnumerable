import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestUnionMethod:
    def test_with_comparer(self) -> None:
        first_object = PurePythonEnumerable(*(items := tuple(range(7))))
        second_object = PurePythonEnumerable(*(-i for i in items))

        res = first_object.union(
            second_object, comparer=lambda x, y: abs(x) == abs(y)
        )

        assert res.source == items

    def test_without_comparer(self) -> None:
        first_object = PurePythonEnumerable(*tuple(range(half := 7)))
        second_object = PurePythonEnumerable(
            *(items := tuple(range(half * 2)))
        )

        res = first_object.union(second_object)

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
