from pyenumerable.implementations.pure_python import PurePythonAssociable


class TestConstructor:
    def test_initialization(self) -> None:
        obj: PurePythonAssociable[str, int] = PurePythonAssociable(
            key := "Key"
        )

        assert obj.key == key
