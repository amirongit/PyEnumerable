from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestZipMethod:
    def test_zip(self) -> None:
        first_object = PurePythonEnumerable(*(first_items := tuple(range(7))))
        second_object = PurePythonEnumerable(
            *(second_items := tuple(range(7, 16)))
        )

        res = first_object.zip(second_object)

        assert res.source == tuple(zip(first_items, second_items))
