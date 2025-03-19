from math import ceil

from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestChunkMethod:
    def test_chunk(self) -> None:
        obj = PurePythonEnumerable(*range(length := 7))

        res = obj.chunk(size := 3)

        assert len(res) == ceil(length / size)
        assert len(res[-1].source) == 1
