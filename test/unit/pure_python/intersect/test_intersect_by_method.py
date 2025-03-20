from pyenumerable.implementations.pure_python import PurePythonEnumerable
from test.unit.pure_python.test_utility import Person, Point


class TestIntersectByMethod:
    def test_when_self_empty(self) -> None:
        first_object = PurePythonEnumerable(Point(0, 1), Point(1, 0))
        second_object: PurePythonEnumerable[Point] = PurePythonEnumerable()

        res = first_object.intersect_by(second_object, lambda point: point.y)

        assert res.source == ()

    def test_when_second_empty(self) -> None:
        first_object: PurePythonEnumerable[Point] = PurePythonEnumerable()
        second_object = PurePythonEnumerable(Point(0, 1), Point(1, 0))

        res = first_object.intersect_by(second_object, lambda point: point.y)

        assert res.source == ()

    def test_without_comparer(self) -> None:
        first_object = PurePythonEnumerable(
            first := Person("john doe", 12, Person("marray doe", 27)),
            Person("jane doe", 10, Person("larry doe", 31)),
            Person("james doe", 11, None),
            second := Person("jacob doe", 17, Person("harry doe", 41)),
            third := Person(" doe", 14, Person("jerry doe", 34)),
        )
        second_object = PurePythonEnumerable(
            Person("john doe", 12, Person("arry doe", 27)),
            Person("jane doe", 10, Person("curry doe", 35)),
            Person("jacob doe", 17, Person("harry doe", 41)),
            Person(" doe", 14, Person("jerry doe", 34)),
        )

        res = first_object.intersect_by(
            second_object,
            lambda person: None
            if person.parent is None
            else person.parent.age,
        )

        assert res.source == (first, second, third)

    def test_with_comparer(self) -> None:
        first_object = PurePythonEnumerable(
            first := Point(5, 1),
            Point(6, 1),
            Point(3, 3),
            Point(4, 5),
            second := Point(2, 7),
            third := Point(3, 9),
        )
        second_object = PurePythonEnumerable(
            Point(4, -1), Point(3, 2), Point(1, -7), Point(2, -9), Point(5, -8)
        )

        res = first_object.intersect_by(
            second_object,
            lambda point: point.y,
            comparer=lambda first_y, second_y: abs(first_y) == abs(second_y),
        )

        assert res.source == (first, second, third)
