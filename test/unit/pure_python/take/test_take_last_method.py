from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestTakeLastMethod:
    def test_functionality(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(25))))

        res = obj.take_last(count := 16)

        assert res.source == items[-count:]
