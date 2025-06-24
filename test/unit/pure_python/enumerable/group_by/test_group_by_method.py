from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestGroupByMethod:
    def test_without_comparer(self) -> None:
        number_of_groups = 2
        first_group_key, number_of_first_group_members = 1, 3
        second_group_key, number_of_second_group_members = 2, 2
        obj = PurePythonEnumerable(
            *(
                Point(i, first_group_key)
                for i in range(number_of_first_group_members)
            ),
            *(
                Point(i, second_group_key)
                for i in range(number_of_second_group_members)
            ),
        )

        res = obj.group_by(lambda point: point.y)

        first_group_index, second_group_index = 0, 1
        assert len(res.source) == number_of_groups
        assert (
            len(res.source[first_group_index].source)
            == number_of_first_group_members
        )
        assert (
            len(res.source[second_group_index].source)
            == number_of_second_group_members
        )
        assert all(
            p.y == first_group_key
            for p in res.source[first_group_index].source
        )
        assert all(
            p.y == second_group_key
            for p in res.source[second_group_index].source
        )
        assert res.source[first_group_index].key == first_group_key
        assert res.source[second_group_index].key == second_group_key

    def test_with_comparer(self) -> None:
        number_of_groups = 2
        (
            first_group_key,
            number_of_first_half_of_first_group_members,
            number_of_second_half_of_first_group_members,
        ) = 1, 3, 3
        (
            second_group_key,
            number_of_first_half_of_second_group_members,
            number_of_second_half_of_second_group_members,
        ) = 2, 2, 2
        obj = PurePythonEnumerable(
            *(
                tuple(
                    Point(i, first_group_key)
                    for i in range(number_of_first_half_of_first_group_members)
                )
                + tuple(
                    Point(i, -first_group_key)
                    for i in range(
                        number_of_second_half_of_first_group_members
                    )
                )
            ),
            *(
                tuple(
                    Point(i, second_group_key)
                    for i in range(
                        number_of_first_half_of_second_group_members
                    )
                )
                + tuple(
                    Point(i, -second_group_key)
                    for i in range(
                        number_of_second_half_of_second_group_members
                    )
                )
            ),
        )

        res = obj.group_by(
            lambda point: point.y,
            comparer=lambda first_y, second_y: abs(first_y) == abs(second_y),
        )

        first_group_index, second_group_index = 0, 1
        assert len(res.source) == number_of_groups
        assert (
            len(res.source[first_group_index].source)
            == number_of_first_half_of_first_group_members
            + number_of_second_half_of_first_group_members
        )
        assert (
            len(res.source[second_group_index].source)
            == number_of_first_half_of_second_group_members
            + number_of_second_half_of_second_group_members
        )
        assert all(
            abs(p.y) == abs(first_group_key)
            for p in res.source[first_group_index].source
        )
        assert all(
            abs(p.y) == abs(second_group_key)
            for p in res.source[second_group_index].source
        )
        assert res.source[first_group_index].key == first_group_key
        assert res.source[second_group_index].key == second_group_key
