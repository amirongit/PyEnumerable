import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestSingleMethod:
    def test_exc_raise_without_predicate_when_multiple_items(self) -> None:
        obj = PurePythonEnumerable(1, 2, 3)

        with pytest.raises(ValueError):  # noqa: PT011
            obj.single()

    def test_exc_raise_without_predicate_when_no_items(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        with pytest.raises(ValueError):  # noqa: PT011
            obj.single()

    def test_exc_raise_with_predicate_when_multiple_items(self) -> None:
        obj = PurePythonEnumerable(1, 2, 3)

        with pytest.raises(ValueError):  # noqa: PT011
            obj.single(lambda x: x % 2 != 0)

    def test_exc_raise_with_predicate_when_no_items(self) -> None:
        obj = PurePythonEnumerable(1, 2, 3)

        with pytest.raises(ValueError):  # noqa: PT011
            obj.single(lambda x: x == 0)

    def test_with_predicate(self) -> None:
        obj = PurePythonEnumerable(1, satisfier := 2, 3)

        res = obj.single(lambda x: x % 2 == 0)

        assert res == satisfier

    def test_without_predicate(self) -> None:
        obj = PurePythonEnumerable(item := 7)

        res = obj.single()

        assert res == item
