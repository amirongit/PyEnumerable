from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestOfTypeMethod:
    def test_of_type(self) -> None:
        obj = PurePythonEnumerable(
            zero := 0, None, "one", two := 2, three := 3
        )

        res = obj.of_type(int)

        assert res.source == (zero, two, three)
