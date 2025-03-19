from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestUnionMethod:
    def test_without_comparer(self) -> None:
        first_object = PurePythonEnumerable(*range(end := 7))
        second_object = PurePythonEnumerable(*range(start := 3, 9))

        res = first_object.union(second_object)

        assert res.source == tuple(range(start, end))

    def test_with_comparer(self) -> None:
        first_object = PurePythonEnumerable(
            first := Point(0, 1),
            Point(3, 1),
            Point(0, 3),
            Point(0, 4),
            second := Point(0, 7),
            third := Point(0, 9),
        )
        second_object = PurePythonEnumerable(
            Point(0, -2),
            Point(0, 1),
            Point(0, 5),
            Point(0, 7),
            Point(0, 9),
        )

        res = first_object.union(
            second_object,
            comparer=lambda first_point, second_point: first_point.y
            == second_point.y,
        )

        assert res.source == (first, second, third)
