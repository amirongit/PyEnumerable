from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestTakeMethod:
    def test_with_count(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(25))))

        res = obj.take(count := 7)

        assert res.source == items[:count]

    def test_with_range(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(25))))

        res = obj.take(start := 7, end := 16)

        assert res.source == items[start:end]
