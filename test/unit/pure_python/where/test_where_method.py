from pyenumerable.implementations.pure_python import PurePythonEnumerable


class TestWhereMethod:
    def test_functionality(self) -> None:
        obj = PurePythonEnumerable(*(items := range(700)))

        res = obj.where(predicate := lambda _, v: v % 5 == 0)

        assert res.source == tuple(
            en[1] for en in filter(
                lambda i: predicate(i[0], i[1]),
                enumerate(items),
            )
        )
