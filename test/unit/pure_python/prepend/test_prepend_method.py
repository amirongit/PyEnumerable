from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestPrependMethod:
    def test_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.prepend(element := 0)

        assert res.source[0] == element

    def test_when_not_empty(self) -> None:
        obj = PurePythonEnumerable(*range(7))

        res = obj.prepend(element := -1)

        assert res.source[0] == element
