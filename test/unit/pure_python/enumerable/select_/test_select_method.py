from collections.abc import Callable

from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestSelectMethod:
    def test_select(self) -> None:
        obj = PurePythonEnumerable(
            *(items := (-4, -2, 4, -9, -3, -4, -4, -10, 7)),
        )

        res = obj.select(TestSelectMethod.combine_index_and_value)

        assert res.source == tuple(
            TestSelectMethod.combine_index_and_value(i, v)
            for i, v in enumerate(items)
        )

    @staticmethod
    def combine_index_and_value(index: int, value: int) -> str:
        return f"{index}: {value}"
