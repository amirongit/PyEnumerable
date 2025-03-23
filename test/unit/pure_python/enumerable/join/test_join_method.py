from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestJoinMethod:
    def test_without_outcaster(self) -> None:
        first_group_key = 1
        second_group_key = 3

        first_object = PurePythonEnumerable(
            fgfo := Point(0, first_group_key),
            sgfo := Point(0, second_group_key),
            sgso := Point(1, second_group_key),
        )
        second_object = PurePythonEnumerable(
            fgfi := Point(first_group_key, 0),
            fgsi := Point(first_group_key, 1),
            sgfi := Point(second_group_key, 0),
        )

        res = first_object.join(
            second_object,
            lambda point: point.y,
            lambda point: point.x,
            lambda outer_point, inner_point: (outer_point, inner_point),
        )

        assert res.source == (
            (fgfo, fgfi),  # (first group first outer, first group first inner)
            (
                fgfo,
                fgsi,
            ),  # (first group first outer, first group second inner)
            (
                sgfo,
                sgfi,
            ),  # (second group first outer, second group first inner)
            (
                sgso,
                sgfi,
            ),  # (second group second outer, second group first inner)
        )

    def test_with_outcaster(self) -> None:
        first_group_key = 1
        second_group_key = 3

        first_object = PurePythonEnumerable(
            fgfo := Point(0, first_group_key),
            Point(0, 2),
            Point(1, 2),
            sgfo := Point(0, second_group_key),
            sgso := Point(1, second_group_key),
        )
        second_object = PurePythonEnumerable(
            fgfi := Point(first_group_key, 0),
            fgsi := Point(first_group_key, 1),
            Point(4, 0),
            Point(4, 1),
            sgfi := Point(second_group_key, 0),
        )

        res = first_object.join(
            second_object,
            lambda point: point.y,
            lambda point: point.x,
            lambda outer_point, inner_point: (outer_point, inner_point),
        )

        assert res.source == (
            (fgfo, fgfi),  # (first group first outer, first group first inner)
            (
                fgfo,
                fgsi,
            ),  # (first group first outer, first group second inner)
            (
                sgfo,
                sgfi,
            ),  # (second group first outer, second group first inner)
            (
                sgso,
                sgfi,
            ),  # (second group second outer, second group first inner)
        )
