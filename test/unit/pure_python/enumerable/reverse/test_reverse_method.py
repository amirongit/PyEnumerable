from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestReverseMethod:
    def test_reverse(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(7))))

        res = obj.reverse()

        assert res.source == tuple(reversed(items))
