import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestSumMethod:
    def test_exc_raise_with_bad_type(self) -> None:
        obj = PurePythonEnumerable("should", "not", "work")

        with pytest.raises(TypeError):
            obj.sum()

    def test_functionality(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(7))))

        res = obj.sum()

        assert res == sum(items)
