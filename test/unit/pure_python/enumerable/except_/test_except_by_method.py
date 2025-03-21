from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestExceptByMethod:
    def test_except_by(self) -> None:
        first_object = PurePythonEnumerable(
            Point(0, 1),
            first := Point(3, 2),
            Point(4, 5),
            second := Point(7, 6),
        )
        second_object = PurePythonEnumerable(
            Point(3, 5), Point(8, 9), Point(-1, 1), Point(4, 7)
        )

        res = first_object.except_by(second_object, lambda point: point.y)

        assert res.source == (first, second)
