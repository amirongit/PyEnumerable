from math import ceil

from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestChunkMethod:
    def test_chunk(self) -> None:
        obj = PurePythonEnumerable(
            one := 1,
            two := 2,
            three := 3,
            four := 4,
            five := 5,
            six := 6,
            seven := 7
        )

        res = obj.chunk(size := 3)

        assert len(res) == ceil(len(obj.source) / size)
        assert res[0].source == (one, two, three)
        assert res[1].source == (four, five, six)
        assert res[2].source == (seven,)
