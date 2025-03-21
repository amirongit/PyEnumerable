from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestContainsMethod:
    def test_positive(self) -> None:
        obj = PurePythonEnumerable(
            Person("john doe", 14),
            Person("jane doe", 12),
        )

        assert (
            obj.contains(
                Person("john doe", 14),
                comparer=lambda first, second: (first.name == second.name)
                and (first.age == second.age),
            )
            is True
        )

    def test_negative(self) -> None:
        obj = PurePythonEnumerable(
            Person("john doe", 14),
            Person("jane doe", 12),
        )

        assert (
            obj.contains(
                Person("john doe", 23),
                comparer=lambda first, second: (first.name == second.name)
                and (first.age == second.age),
            )
            is False
        )
