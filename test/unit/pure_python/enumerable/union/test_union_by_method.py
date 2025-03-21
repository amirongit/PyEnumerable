from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestUnionByMethod:
    def test_union_by(self) -> None:
        first_object = PurePythonEnumerable(
            *(
                first_items := (
                    Point(0, 1),
                    Point(0, 2),
                    Point(0, 3),
                )
            )
        )
        second_object = PurePythonEnumerable(
            *(
                second_items := (
                    Point(0, -4),
                    Point(0, -5),
                    Point(0, -6),
                )
            )
        )

        res = first_object.union_by(
            second_object,
            lambda point: point.y,
            comparer=lambda first_y, second_y: abs(first_y) == abs(second_y),
        )

        assert res.source == first_items + second_items

    def test_overlap_remove_for_self(self) -> None:
        first_object = PurePythonEnumerable(
            first := Point(0, 1),
            Point(1, 1),
            second := Point(0, 3),
        )
        second_object = PurePythonEnumerable(
            third := Point(4, 5),
            fourth := Point(6, 7),
        )

        res = first_object.union_by(second_object, lambda point: point.y)

        assert res.source == (first, second, third, fourth)

    def test_overlap_remove_for_second(self) -> None:
        first_object = PurePythonEnumerable(
            first := Point(0, 1),
            second := Point(0, 3),
        )
        second_object = PurePythonEnumerable(
            third := Point(4, 5),
            Point(5, 5),
            fourth := Point(6, 7),
        )

        res = first_object.union_by(second_object, lambda point: point.y)

        assert res.source == (first, second, third, fourth)
