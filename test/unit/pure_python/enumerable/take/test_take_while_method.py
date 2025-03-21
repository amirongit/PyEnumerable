from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestTakeWhileMethod:
    def test_with_alway_true_predicate(self) -> None:
        obj = PurePythonEnumerable(*(items := tuple(range(7))))

        res = obj.take_while(lambda _i, _v: True)

        assert res.source == items

    def test_with_alway_false_predicate(self) -> None:
        obj = PurePythonEnumerable(*range(7))

        res = obj.take_while(lambda _i, _v: False)

        assert res.source == ()

    def test_with_proper_predicate(self) -> None:
        obj = PurePythonEnumerable(
            from_iterable=(
                odds := tuple(range(1, 10, 2)),
                tuple(range(0, 10, 2)),
            ),
        )

        res = obj.take_while(lambda _, v: v % 2 == 1)

        assert res.source == odds
