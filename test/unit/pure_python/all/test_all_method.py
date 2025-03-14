from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestAllMethod:
    def test_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.all(lambda _: False)

        assert res is True

    def test_pass(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable(
            *range(threshold := 7),
        )

        res = obj.all(lambda x: x <= threshold)

        assert res is True

    def test_fail(self) -> None:
        obj = PurePythonEnumerable(
            Person("john", 14, Person("marry", 36)),
            Person("junior", 14, Person("james", 36)),
            Person("larry", 6),
            Person("jane", 6, Person("harry", 28)),
        )

        res = obj.all(lambda person: person.parent is not None)

        assert res is False
