from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestAllMethod:
    def test_without_predicate_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.all()

        assert res is True

    def test_pass_without_predicate(self) -> None:
        obj = PurePythonEnumerable(True, True, True)  # noqa: FBT003

        res = obj.all()

        assert res is True

    def test_fail_without_predicate(self) -> None:
        obj = PurePythonEnumerable(True, None, False)  # noqa: FBT003

        res = obj.all()

        assert res is False

    def test_with_predicate_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.all(lambda _: False)

        assert res is True

    def test_pass_with_predicate(self) -> None:
        obj = PurePythonEnumerable(*range(threshold := 7))

        res = obj.all(lambda x: x <= threshold)

        assert res is True

    def test_fail_with_predicate(self) -> None:
        obj = PurePythonEnumerable(
            Person("john", 14, Person("marry", 36)),
            Person("junior", 14, Person("james", 36)),
            Person("larry", 6),
            Person("jane", 6, Person("harry", 28)),
        )

        res = obj.all(lambda person: person.parent is not None)

        assert res is False
