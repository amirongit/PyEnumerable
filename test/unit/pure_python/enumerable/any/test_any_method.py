from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person


class TestAnyMethod:
    def test_without_predicate_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.any_()

        assert res is False

    def test_pass_without_predicate(self) -> None:
        obj = PurePythonEnumerable(False, False, True)  # noqa: FBT003

        res = obj.any_()

        assert res is True

    def test_fail_without_predicate(self) -> None:
        obj = PurePythonEnumerable(None, False, False)  # noqa: FBT003

        res = obj.any_()

        assert res is False

    def test_with_predicate_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.any_(lambda _: True)

        assert res is False

    def test_pass_with_predicate(self) -> None:
        obj = PurePythonEnumerable(*range((threshold := 7) + 1))

        res = obj.any_(lambda x: x == threshold)

        assert res is True

    def test_fail_with_predicate(self) -> None:
        obj = PurePythonEnumerable(
            Person("john doe", 14, Person("marry doe", 36)),
            Person("junior doe", 14, Person("james doe", 36)),
            Person("larry doe", 6),
            Person("jane doe", 6, Person("harry doe", 28)),
        )

        res = obj.any_(
            lambda person: (
                person.parent is not None and person.parent.parent is not None
            ),
        )

        assert res is False
