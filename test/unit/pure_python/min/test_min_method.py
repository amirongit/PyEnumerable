import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestMinMethod:
    def test_exc_raise_when_empty(self) -> None:
        obj: PurePythonEnumerable[Point] = PurePythonEnumerable()

        with pytest.raises(ValueError):  # noqa: PT011
            obj.min_()

    def test_exc_raise_when_uncomparable(self) -> None:
        obj = PurePythonEnumerable(Point(1, 2), Point(3, 4))

        with pytest.raises(TypeError):
            obj.min_()

    def test_with_comparer(self) -> None:
        obj = PurePythonEnumerable(minimum := Point(4, 5), Point(6, 3))

        res = obj.min_(comparer=lambda first, second: first.x < second.x)

        assert res is minimum

    def test_without_comparer(self) -> None:
        obj = PurePythonEnumerable(minimum := 6, 8, 10, 9, 7)

        res = obj.min_()

        assert res == minimum
