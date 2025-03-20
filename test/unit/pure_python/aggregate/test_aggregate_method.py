import pytest
from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestAggregateMethod:
    def test_exc_raise_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        with pytest.raises(ValueError):  # noqa: PT011
            obj.aggregate(lambda _, __: 0)

    def test_without_seed(self) -> None:
        obj = PurePythonEnumerable(*(items := range(7)))

        res = obj.aggregate(lambda x, y: x + y)

        assert res == sum(items)

    def test_with_seed(self) -> None:
        obj = PurePythonEnumerable(*(items := range(7)))

        res = obj.aggregate(lambda x, y: x + y, seed=10)

        assert res == 10 + sum(items)
