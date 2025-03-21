import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestSingleOrDefaultMethod:
    def test_exc_raise_without_predicate_when_multiple_items(self) -> None:
        obj = PurePythonEnumerable(1, 2, 3)

        with pytest.raises(ValueError):  # noqa: PT011
            obj.single_or_deafult(7)

    def test_exc_raise_with_predicate_when_multiple_items(self) -> None:
        obj = PurePythonEnumerable(1, 2, 3)

        with pytest.raises(ValueError):  # noqa: PT011
            obj.single_or_deafult(7, lambda x: x % 2 != 0)

    def test_default_without_predicate(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.single_or_deafult(default := 7)

        assert res == default

    def test_default_with_predicate(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable(1, 2, 3)

        res = obj.single_or_deafult(default := 7, lambda x: x == 0)

        assert res == default

    def test_without_predicate(self) -> None:
        obj = PurePythonEnumerable(item := 7)

        res = obj.single_or_deafult(0)

        assert res == item

    def test_with_predicate(self) -> None:
        obj = PurePythonEnumerable(4, item := 7, 10)

        res = obj.single_or_deafult(0, lambda x: x % 2 != 0)

        assert res == item
