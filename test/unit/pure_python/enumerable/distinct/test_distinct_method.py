import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person, Point


class TestDistinctMethod:
    def test_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.distinct()

        assert res.source == ()

    def test_without_comparer(self) -> None:
        obj = PurePythonEnumerable(
            from_iterable=(items := tuple(range(7)), items),
        )

        res = obj.distinct()

        assert res.source == items

    def test_with_comparer(self) -> None:
        obj = PurePythonEnumerable(
            first := Point(3, 4),
            Point(1, 4),
            second := Point(3, 5),
            Point(4, 5),
            third := Point(3, 6),
            Point(0, 6),
            fourth := Point(3, 7),
            Point(10, 7),
        )

        res = obj.distinct(
            comparer=lambda first_point, second_point: first_point.y
            == second_point.y,
        )

        assert res.source == (first, second, third, fourth)
