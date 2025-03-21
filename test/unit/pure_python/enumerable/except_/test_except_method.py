from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestExceptMethod:
    def test_without_comparer(self) -> None:
        first_object = PurePythonEnumerable(*range(7))
        second_object = PurePythonEnumerable(*range(start := 3, 9))

        res = first_object.except_(second_object)

        assert res.source == tuple(range(start))

    def test_with_comparer(self) -> None:
        first_object = PurePythonEnumerable(
            Point(0, 1),
            first := Point(1, 3),
            Point(3, 5),
            second := Point(8, 12),
        )
        second_object = PurePythonEnumerable(
            Point(4, 18), Point(3, 1), Point(0, 0), Point(1, 5)
        )

        res = first_object.except_(
            second_object,
            comparer=lambda first_point, second_point: first_point.y
            == second_point.y,
        )

        assert res.source == (first, second)
