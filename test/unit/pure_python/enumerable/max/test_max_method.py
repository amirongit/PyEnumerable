import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestMaxMethod:
    def test_exc_raise_when_empty(self) -> None:
        obj: PurePythonEnumerable[Point] = PurePythonEnumerable()

        with pytest.raises(ValueError):  # noqa: PT011
            obj.max_()

    def test_exc_raise_when_uncomparable(self) -> None:
        obj = PurePythonEnumerable(Point(1, 2), Point(3, 4))

        with pytest.raises(TypeError):
            obj.max_()

    def test_with_comparer(self) -> None:
        obj = PurePythonEnumerable(Point(4, 5), maximum := Point(6, 3))

        res = obj.max_(comparer=lambda first, second: first.x > second.x)

        assert res is maximum

    def test_without_comparer(self) -> None:
        obj = PurePythonEnumerable(6, 8, maximum := 10, 9, 7)

        res = obj.max_()

        assert res == maximum
