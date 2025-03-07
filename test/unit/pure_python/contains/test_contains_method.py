from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestContainsMethod:
    def test_positive_without_comparer(self) -> None:
        existing_item = "existing-item"
        obj = PurePythonEnumerable(
            "not-being-tested",
            "also-not-being-tested",
            existing_item,
        )

        assert obj.contains(existing_item) is True

    def test_positive_with_comparer(self) -> None:
        obj = PurePythonEnumerable(
            Person("john", 14),
            Person("jane", 12),
        )

        assert obj.contains(
            Person("john", 14),
            comparer=lambda first, second: (
                first.name == second.name
            ) and (
                first.age == second.age
            ),
        ) is True

    def test_negative_without_comparer(self) -> None:
        obj = PurePythonEnumerable(
            "not-being-tested",
            "also-not-being-tested",
        )

        assert obj.contains("non-existing-item") is False

    def test_negative_with_comparer(self) -> None:
        obj = PurePythonEnumerable(
            Person("john", 14),
            Person("jane", 12),
        )

        assert obj.contains(
            Person("john", 23),
            comparer=lambda first, second: (
                first.name == second.name
            ) and (
                first.age == second.age
            ),
        ) is False
