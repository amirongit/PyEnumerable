from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestEnumerableConstructor:
    def test_initialization_with_raw_items(self) -> None:
        obj = PurePythonEnumerable(*(items := (6, -10, -4, 0, 4)))

        assert items == obj.source

    def test_initialization_with_packed_items(self) -> None:
        obj = PurePythonEnumerable(
            from_iterable=(
                (first := (2, -1, 2, 3, 3, -2, 7), second := (3, 9, 4, 5, -8))
            ),
        )

        assert first + second == obj.source

    def test_initialization_with_raw_and_packed_items(self) -> None:
        obj = PurePythonEnumerable(
            *(raw := (-7, 1, -9, -9, -5)),
            from_iterable=(packed := (5, 6, -9, 2, -5, -10, 2, -8, 4),),
        )

        assert raw + packed == obj.source
