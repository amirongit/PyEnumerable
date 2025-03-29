from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestGroupJoinMethod:
    def test_group_join(self) -> None:
        first_object = PurePythonEnumerable(
            first_parent := Person("john doe", 32),
            second_parent := Person("jane doe", 28),
        )
        second_object = PurePythonEnumerable(
            first_child := Person("larry doe", 12, first_parent),
            second_child := Person("jerry doe", 13, first_parent),
            third_child := Person("marry doe", 14, second_parent),
            fourth_child := Person("james doe", 15, second_parent),
            fifth_child := Person("james doe", 16, second_parent),
        )

        res = first_object.group_join(
            second_object,
            lambda parent: parent.name,
            lambda child: child.parent.name
            if child.parent is not None
            else None,
            lambda parent, children: (parent, children.source),
        )

        assert res.source == (
            (first_parent, (first_child, second_child)),
            (second_parent, (third_child, fourth_child, fifth_child)),
        )

    def test_overlap_remove(self) -> None:
        first_object = PurePythonEnumerable(
            first_parent := Person("john doe", 32),
            Person("jane doe", 32),
        )
        second_object = PurePythonEnumerable(
            Person("larry doe", 12, first_parent),
            Person("jerry doe", 13, first_parent),
        )

        res = first_object.group_join(
            second_object,
            lambda parent: parent.age,
            lambda child: child.parent.age
            if child.parent is not None
            else None,
            lambda parent, children: (parent.age, children.source),
        )

        assert len(res.source) == 1
