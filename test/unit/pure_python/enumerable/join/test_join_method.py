from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestJoinMethod:
    def test_without_outcaster(self) -> None:
        first_group_key = 1
        second_group_key = 3

        first_object = PurePythonEnumerable(
            first_group_first_outer := Point(0, first_group_key),
            second_group_first_outer := Point(0, second_group_key),
            second_group_second_outer := Point(1, second_group_key),
        )
        second_object = PurePythonEnumerable(
            first_group_first_inner := Point(first_group_key, 0),
            first_group_second_inner := Point(first_group_key, 1),
            second_group_first_inner := Point(second_group_key, 0),
        )

        res = first_object.join(
            second_object,
            lambda point: point.y,
            lambda point: point.x,
            lambda outer_point, inner_point: (outer_point, inner_point),
        )

        assert res.source == (
            (first_group_first_outer, first_group_first_inner),
            (first_group_first_outer, first_group_second_inner),
            (second_group_first_outer, second_group_first_inner),
            (second_group_second_outer, second_group_first_inner),
        )

    def test_with_outcaster(self) -> None:
        first_group_key = 1
        second_group_key = 3

        first_object = PurePythonEnumerable(
            first_group_first_outer := Point(0, first_group_key),
            Point(0, 2),
            Point(1, 2),
            second_group_first_outer := Point(0, second_group_key),
            second_group_second_outer := Point(1, second_group_key),
        )
        second_object = PurePythonEnumerable(
            first_group_first_inner := Point(first_group_key, 0),
            first_group_second_inner := Point(first_group_key, 1),
            Point(4, 0),
            Point(4, 1),
            second_group_first_inner := Point(second_group_key, 0),
        )

        res = first_object.join(
            second_object,
            lambda point: point.y,
            lambda point: point.x,
            lambda outer_point, inner_point: (outer_point, inner_point),
        )

        assert res.source == (
            (first_group_first_outer, first_group_first_inner),
            (first_group_first_outer, first_group_second_inner),
            (second_group_first_outer, second_group_first_inner),
            (second_group_second_outer, second_group_first_inner),
        )
