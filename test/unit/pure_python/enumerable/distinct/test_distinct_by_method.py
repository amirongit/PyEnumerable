import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person, Point


class TestDistinctByMethod:
    def test_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.distinct_by(lambda x: x**2)

        assert res.source == ()

    def test_without_comparer(self) -> None:
        obj = PurePythonEnumerable(
            from_iterable=(items := tuple(range(7)), [-i for i in items]),
        )

        res = obj.distinct_by(lambda i: abs(i))

        assert res.source == items

    def test_with_comparer(self) -> None:
        obj = PurePythonEnumerable(
            first := Point(3, 4),
            Point(1, -4),
            second := Point(3, 5),
            Point(4, -5),
            third := Point(3, 6),
            Point(0, -6),
            fourth := Point(3, 7),
            Point(10, -7),
        )

        res = obj.distinct_by(
            lambda point: point.y,
            comparer=lambda first_y, second_y: first_y**2 == second_y**2,
        )

        assert res.source == (first, second, third, fourth)
