from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestSkipLastMethod:
    def test_functionality(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(25))))

        res = obj.skip_last(count := 16)

        assert res.source == items[:-count]
