import pytest

from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestAverageMethod:
    def test_average(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(7))))

        res = obj.average()

        assert res == sum(items) / len(items)

    def test_exc_raise_when_unexecutable(self) -> None:
        obj = PurePythonEnumerable("should", "not", "work")

        with pytest.raises(TypeError):
            obj.average()
