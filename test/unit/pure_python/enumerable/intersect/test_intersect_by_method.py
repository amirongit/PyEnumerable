from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person, Point


class TestIntersectByMethod:
    def test_when_self_empty(self) -> None:
        first_object = PurePythonEnumerable(Point(0, 1), Point(1, 0))
        second_object: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = first_object.intersect_by(second_object, lambda point: point.y)

        assert res.source == ()

    def test_when_second_empty(self) -> None:
        first_object: PurePythonEnumerable[int] = PurePythonEnumerable()
        second_object = PurePythonEnumerable(Point(0, 1), Point(1, 0))

        res = first_object.intersect_by(second_object, lambda x: Point(x, 0))

        assert res.source == ()

    def test_with_comparer(self) -> None:
        first_object = PurePythonEnumerable(
            first := Point(5, 1),
            Point(3, 3),
            Point(4, 5),
            second := Point(2, 7),
            third := Point(3, 9),
        )
        second_object = PurePythonEnumerable(-1, -7, -9)

        res = first_object.intersect_by(
            second_object,
            lambda point: point.y,
            comparer=lambda first, second: abs(first) == abs(second),
        )

        assert res.source == (first, second, third)

    def test_without_comparer(self) -> None:
        first_object = PurePythonEnumerable(
            first := Point(5, 1),
            Point(3, 3),
            Point(4, 5),
            second := Point(2, 7),
            third := Point(3, 9),
        )
        second_object = PurePythonEnumerable(1, 7, 9)

        res = first_object.intersect_by(second_object, lambda point: point.y)

        assert res.source == (first, second, third)

    def test_overlap_remove(self) -> None:
        first_object = PurePythonEnumerable(
            first := Point(5, 1),
            Point(6, 1),
            second := Point(2, 7),
            third := Point(3, 9),
        )
        second_object = PurePythonEnumerable(-1, -7, -9)

        res = first_object.intersect_by(
            second_object,
            lambda point: point.y,
            comparer=lambda first_y, second_y: abs(first_y) == abs(second_y),
        )

        assert res.source == (first, second, third)
