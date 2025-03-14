from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestAnyMethod:
    def test_without_predicate_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.any()

        assert res is False

    def test_pass_without_predicate(self) -> None:
        obj = PurePythonEnumerable(False, False, True)  # noqa: FBT003

        res = obj.any()

        assert res is True

    def test_fail_without_predicate(self) -> None:
        obj = PurePythonEnumerable(None, False, False)  # noqa: FBT003

        res = obj.any()

        assert res is False

    def test_with_predicate_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.any(lambda _: True)

        assert res is False

    def test_pass_with_predicate(self) -> None:
        obj = PurePythonEnumerable(*range((threshold := 7) + 1))

        res = obj.any(lambda x: x == threshold)

        assert res is True

    def test_fail_with_predicate(self) -> None:
        obj = PurePythonEnumerable(
            Person("john", 14, Person("marry", 36)),
            Person("junior", 14, Person("james", 36)),
            Person("larry", 6),
            Person("jane", 6, Person("harry", 28)),
        )

        res = obj.any(
            lambda person: (
                person.parent is not None and person.parent.parent is not None
            ),
        )

        assert res is False
