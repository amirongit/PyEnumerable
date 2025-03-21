import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person, Point


class TestOrderByDescendingMethod:
    def test_when_empty(self) -> None:
        obj: PurePythonEnumerable[Person] = PurePythonEnumerable()

        res = obj.order_by_descending(lambda person: person.age)

        assert res.source == ()

    def test_exc_raise_when_uncomparable(self) -> None:
        obj = PurePythonEnumerable(
            Person("jane doe", 25, Person("james doe", 30)),
            Person("john doe", 17, Person("jacob doe", 35)),
        )

        with pytest.raises(TypeError):
            obj.order_by_descending(lambda person: person.parent)

    def test_without_comparer(self) -> None:
        obj = PurePythonEnumerable(
            fifth := Point(0, 5),
            second := Point(0, 2),
            fourth := Point(0, 4),
            first := Point(0, 1),
            third := Point(0, 3),
        )

        res = obj.order_by_descending(lambda point: point.y)

        assert res.source == (fifth, fourth, third, second, first)

    def test_with_comparer(self) -> None:
        obj = PurePythonEnumerable(
            Person("john doe", 17),
            Person("jane doe", 31),
            second := Person("james doe", 28, Person("harry doe", 36)),
            third := Person("jade doe", 24, Person("larry doe", 42)),
            first := Person("jacob doe", 14, Person("marry doe", 28)),
        )

        res = obj.order_by_descending(
            lambda person: person.parent,
            comparer=TestOrderByDescendingMethod.parent_age_comparer,
        )

        assert res.source[2:] == (third, second, first)

    @staticmethod
    def parent_age_comparer(
        first_person: Person | None, second_person: Person | None
    ) -> bool:
        if first_person is not None:
            if second_person is not None:
                return first_person.age < second_person.age
            return True

        return True
