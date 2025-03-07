from random import randint

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestCountMethod:
    def test_without_predicate(self) -> None:
        obj = PurePythonEnumerable(*(items := range(randint(25, 50))))

        assert obj.count_() == len(items)

    def test_with_predicate(self) -> None:
        obj = PurePythonEnumerable(
            Person("john", 21),
            Person("jane", 13),
            Person("james", 7),
            Person("marry", 34),
            Person("harry", 17),
            Person("larry", 28),
        )

        age_of_consent = 21
        number_of_fuckable_people = 3

        assert obj.count_(
            lambda p: p.age >= age_of_consent,
        ) == number_of_fuckable_people


