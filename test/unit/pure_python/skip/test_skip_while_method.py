from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestSkipWhileMethod:
    def test_with_alway_true_predicate(self) -> None:
        obj = PurePythonEnumerable(*range(7))

        res = obj.skip_while(lambda _i, _v: True)

        assert res.source == ()

    def test_with_alway_false_predicate(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(7))))

        res = obj.skip_while(lambda _i, _v: False)

        assert res.source == items

    def test_with_proper_predicate(self) -> None:
        obj = PurePythonEnumerable(
            from_iterable=(
                tuple(range(1, 10, 2)),
                evens := tuple(range(0, 10, 2)),
            ),
        )

        res = obj.skip_while(lambda _, v: v % 2 != 0)

        assert res.source == evens
