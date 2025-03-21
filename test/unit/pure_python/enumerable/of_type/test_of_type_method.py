from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestOfTypeMethod:
    def test_capturing_functionality(self) -> None:
        obj = PurePythonEnumerable(None, "first", *(items := (1, 2)))

        res = obj.of_type(int)

        assert len(res.source) == len(items)

    def test_filtering_functionality(self) -> None:
        obj = PurePythonEnumerable(None, "first", two := 2, three := 3)

        res = obj.of_type(int)

        assert set(res.source) == {two, three}
