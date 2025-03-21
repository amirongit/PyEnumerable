from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Point


class TestSequenceEqualMethod:
    def test_pass_without_comparer(self) -> None:
        first_object = PurePythonEnumerable(*range(stop := 7))
        second_object = PurePythonEnumerable(*range(stop))

        res = first_object.sequence_equal(second_object)

        assert res is True

    def test_fail_without_comparer(self) -> None:
        first_object = PurePythonEnumerable(*range(7))
        second_object = PurePythonEnumerable(*range(1, 8))

        res = first_object.sequence_equal(second_object)

        assert res is False

    def test_pass_with_comparer(self) -> None:
        first_object = PurePythonEnumerable(
            Point(0, 1), Point(1, 3), Point(2, 4)
        )
        second_object = PurePythonEnumerable(
            Point(2, 1), Point(1, 3), Point(0, 4)
        )

        res = first_object.sequence_equal(
            second_object,
            comparer=lambda first_point, second_point: first_point.y
            == second_point.y,
        )

        assert res is True

    def test_fail_with_comparer(self) -> None:
        first_object = PurePythonEnumerable(
            Point(0, 1), Point(1, 3), Point(2, 4)
        )
        second_object = PurePythonEnumerable(
            Point(1, 0), Point(3, 1), Point(4, 2)
        )

        res = first_object.sequence_equal(
            second_object,
            comparer=lambda first_point, second_point: first_point.y
            == second_point.y,
        )

        assert res is False

    def test_when_not_equal_length(self) -> None:
        first_object = PurePythonEnumerable(*range(7))
        second_object = PurePythonEnumerable(*range(3))

        res = first_object.sequence_equal(second_object)

        assert res is False
