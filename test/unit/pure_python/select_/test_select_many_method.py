from itertools import chain

from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestSelectManyMethod:
    def test_functionality(self) -> None:
        obj = PurePythonEnumerable(
            *(items := (3, -2, 1, -4, -7, -8, -10, 6, -9)),
        )

        res = obj.select_many(TestSelectManyMethod.combine_index_and_value)

        assert tuple(
            chain.from_iterable(
                (
                    TestSelectManyMethod.combine_index_and_value(i, v) for i,
                    v in enumerate(items)
                ),
            ),
        ) == res.source

    @staticmethod
    def combine_index_and_value(index: int, value: int) -> tuple[int, int]:
        return (index, value)
