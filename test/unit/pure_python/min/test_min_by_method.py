import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestMinByMethod:
    def test_exc_raise_when_empty(self) -> None:
        obj: PurePythonEnumerable[Person] = PurePythonEnumerable()

        with pytest.raises(ValueError):  # noqa: PT011
            obj.min_by(lambda person: person.age)

    def test_exc_raise_when_uncomparable(self) -> None:
        obj = PurePythonEnumerable(
            Person("jane", 4, Person("james", 34)),
            Person("john", 3),
        )

        with pytest.raises(TypeError):
            obj.min_by(lambda person: person.parent)

    def test_with_comparer(self) -> None:
        obj = PurePythonEnumerable(
            minimum := Person("jane", 12, Person("james", 34)),
            Person("john", 4, Person("jessie", 40)),
        )

        res = obj.min_by(
            lambda person: person.parent,
            comparer=TestMinByMethod.age_comparer,
        )

        assert minimum is res

    def test_without_comparer(self) -> None:
        obj = PurePythonEnumerable(
            Person("jane", 12, Person("james", 34)),
            minimum := Person("john", 4, Person("jessie", 40)),
        )

        res = obj.min_by(lambda person: person.age)

        assert res is minimum

    @staticmethod
    def age_comparer(
        first: Person | None,
        second: Person | None,
    ) -> bool:
        if first is None or second is None:
            raise ValueError

        return first.age < second.age
