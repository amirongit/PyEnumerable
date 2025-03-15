from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestAppendMethod:
    def test_when_empty(self) -> None:
        obj: PurePythonEnumerable[int] = PurePythonEnumerable()

        res = obj.append(element := 0)

        assert res.source[0] == element

    def test_when_not_empty(self) -> None:
        obj = PurePythonEnumerable(*range(element := 7))

        res = obj.append(element)

        assert res.source[-1] == element
