from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestCountMethod:
    def test_without_predicate(self) -> None:
        obj = PurePythonEnumerable(*(items := range(25)))

        assert obj.count_() == len(items)

    def test_with_predicate(self) -> None:
        obj = PurePythonEnumerable(
            Person("john doe", 21),
            Person("jane doe", 13),
            Person("james doe", 7),
            Person("marry doe", 34),
            Person("harry doe", 17),
            Person("larry doe", 28),
        )

        age_of_consent = 21
        number_of_fuckable_people = 3

        assert (
            obj.count_(
                lambda person: person.age >= age_of_consent,
            )
            == number_of_fuckable_people
        )
