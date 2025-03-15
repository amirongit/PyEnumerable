from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestConcatMethod:
    def test_concat(self) -> None:
        first = PurePythonEnumerable(
            *(first_items := (-5, 5, -2, 8, 3, -9, 8, 5, -4)),
        )

        second = PurePythonEnumerable(
            *(second_items := (-9, -3, -8, -1, 8, -9)),
        )

        final = first.concat(second)

        assert final.source == first_items + second_items
