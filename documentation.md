# PyEnumerable ![WTFPL License](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)

Implementation of .NET's [IEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1?view=net-9.0) interface in python W/ support for generics.

## Architecture & Design

PyEnumerable follows a relatively simple architecture, mainly because there isn't any reason to do otherwise!<br/>
Extension methods defined by `IEnumerable` interface are grouped by their functionality under protocols located `pyenumerable.protocol` package; The main advantage provided by protocols over ABCs (abstract base classes) is the ability to define overloads w/ different signatures.

### Protocols

#### Common Type Variables Among Protocols

##### `TSource`

Type of items of `self`.

#### Common Arguments Among Methods

##### `comparer`

A callable which accepts two arguments of type `TSource` & returns a `bool` value; The meaning of the returned value is dependant on the context of its method; usually defaults to `lambda i, o: i == o`.

#### `Enumerable`

This protocol consolidates all other protocols into a single one, allowing implementations to reference it instead of listing each individual protocol. This approach minimizes the risk of omitting any methods due to oversight.<br/>
It also enforces the presence of a property called `source` which can be used to access actual items inside an instance of a particular implementation.

#### `Associable`

This protocol is the return type of `group_by` method; It inherits `Enumerable` & enforces an additional property called `key` which can be used to access the common key of a particular group.

#### `SupportsAggregate`

##### `aggregate`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.aggregate(lambda x, y: x + y) == 15
assert one.aggregate(lambda x, y: x + y, seed=10) == 25
```

#### `SupportsAll`

##### `all`

usage:
```py
assert one.source == (True, True)
assert one.all() is True
assert two.source == (True, False)
assert two.all() is False
assert three.source == (1, 2, 3, 4, 5)
assert three.all(lambda x: x < 7) is True
assert three.source == (1, 2, 3, 4, 5)
assert three.all(lambda x: x > 7) is False
```

#### `SupportsAny`

##### `any`

usage:
```py
assert one.source == (True, False)
assert one.any() is True
assert two.source == (False, False)
assert two.any() is False
assert three.source == (1, 2, 3, 4, 5)
assert three.any(lambda x: x == 7) is False
assert four.source == (1, 2, 3, 4, 5)
assert four.any(lambda x: x == 1) is True
```

#### `SupportsAppend`

##### `append`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.append(7).source == (1, 2, 3, 4, 5, 7)
```

#### `SupportsAverage`

##### `average`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.average() == 3.0
```

#### `SupportsChunk`

##### `chunk`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.chunk(2) == (res := (two, three, four))
assert two.source == (1, 2)
assert three.source == (3, 4)
assert four.source == (5,)
```

#### `SupportsConcat`

##### `concat`

usage:
```py
assert one.source == (1, 2, 3)
assert two.source == (4, 5)
assert one.concat(two).source == (1, 2, 3, 4, 5)
```

#### `SupportsContains`

##### `contains`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.contains(3) is True
assert one.contains(7) is False
```

#### `SupportsCount`

##### `count`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.count() == 5
assert one.count(lambda x: x >= 3) == 3
```

#### `SupportsDistinct`

##### `distinct`

usage:
```py
assert one.source == (1, 2, 2, 3, 3, 4, 5)
assert one.distinct().res == (1, 2, 3, 4, 5)
```

##### `distinct_by`

usage:
```py
assert one.source == (1, 2, -1, -2, -3, 4, -5)
assert one.distinct_by(lambda x: abs(x)).res == (1, 2, -3, 4, -5)
```

type parameters:
- `TKey`: Type of key to distinguish items by.

#### `SupportsExcept`

##### `except_`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert two.source == (1, 2, 3)
assert one.except_(two).source == (4, 5)
```

##### `except_by`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (
    Point(1, 1),
    Point(1, 2),
    Point(1, 3),
    Point(1, 4),
    Point(1, 5)
)
assert two.source == (
    Point(2, 1),
    Point(2, 2),
    Point(2, 3),
)
assert one.except_by(two, lambda point: point.y).source == (
    Point(1, 4),
    Point(1, 5)
)
```
type parameters:
- `TKey`: Type of key to identify items by.

#### `SupportsGroupBy`

##### `group_by`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (
    Point(1, 1),
    Point(2, 1),
    Point(3, 2),
    Point(4, 2),
    Point(5, 2),
)
assert one.group_by(lambda point: point.y).source == (two, three)
assert two.key == 1
assert two.source == (Point(1, 1), Point(2, 1))
assert three.key == 2
assert three.source == (Point(3, 2), Point(4, 2), Point(5, 2))
```

type parameters:
- `TKey`: Type of key returned by `key_selector`; Will be used to group items by.

#### `SupportsGroupJoin`

##### `group_join`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (1, 2)
assert two.source == (
    Point(1, 1),
    Point(2, 1),
    Point(3, 2),
    Point(4, 2),
    Point(5, 2),
)
assert one.group_join(
    two,
    lambda x: x,
    lambda point: point.y,
    lambda x, points: (x, points.source)
).source == (
    (1, Point(1, 1), Point(2, 1)),
    (2, Point(3, 2), Point(4, 2), Point(5, 2))
)
```

type parameters:
- `TKey`: Type of keys to group & join items by.
- `TInner`: Type of items of the second enumerable.
- `TResult`: Type of result items.

#### `SupportsIntersect`

##### `intersect`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert two.source == (1, 2, 3)
assert one.intersect(two) == (1, 2, 3)
```

##### `intersect_by`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (
    Point(1, 1),
    Point(1, 2),
    Point(1, 3),
    Point(1, 4),
    Point(1, 5)
)
assert two.source == (1, 2, 3)
assert one.intersect_by(two, lambda point: point.y).source == (
    Point(1, 1),
    Point(1, 2),
    Point(1, 3)
)
```

type parameters:
- `TKey`: Type of key to identify items by.

#### `SupportsJoin`

##### `join`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (
    Point(0, 1),
    Point(0, 2),
    Point(1, 2),
    Point(0, 3),
    Point(1, 1),
)
assert two.source == (
    Point(1, 0),
    Point(1, 1),
    Point(4, 0),
    Point(4, 1),
    Point(3, 0),
)
assert one.join(
    two,
    lambda point: point.y,
    lambda point: point.x,
    lambda outer_point,
    inner_point: (outer_point, inner_point),
).source == (
    (Point(0, 1), Point(1, 0)),
    (Point(0, 1), Point(1, 1)),
    (Point(0, 3), Point(3, 0)),
    (Point(1, 3), Point(3, 0)),
)
```

type parameters:
- `TKey`: Type of keys to join items by.
- `TInner`: Type of items of the second enumerable.
- `TResult`: Type of result items.

#### `SupportsMax`

##### `max_`

usage:
```py
assert one.source == (2, 4, 5, 3, 1)
assert one.max_() == 5
```

##### `max_by`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (
    Point(2, 1),
    Point(4, 1),
    Point(5, 1),
    Point(3, 1),
    Point(1, 1),
)
assert one.max_by(lambda point: point.x) == Point(5, 1)
```

type parameters:
- `TKey`: Type of key to compare items by.

#### `SupportsMin`

##### `min_`

usage:
```py
assert one.source == (5, 3, 1, 2, 4)
assert one.min_() == 1
```

##### `min_by`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (
    Point(5, 1),
    Point(3, 1),
    Point(1, 1),
    Point(2, 1),
    Point(4, 1),
)
assert one.min_by(lambda point: point.x) == Point(1, 1)
```

type parameters:
- `TKey`: Type of key to compare items by.

#### `SupportsOfType`

##### `of_type`

usage:
```py
assert one.source == (0, None, "one", 2, 3)
assert one.of_type(int) == (0, 2, 3)
```

type parameters:
- `TResult`: Type of result items to filter items of enumerable on.

#### `SupportsOrder`

##### `order`
usage:
```py
assert one.source == (1, 2, 5, 4, 3)
assert one.order().source == (1, 2, 3, 4, 5)
```

##### `order_by`
usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (Point(1, 2), Point(1, 3), Point(1, 1))
assert one.order_by(lambda point: point.y).source == (Point(1, 1), Point(1, 2), Point(1, 3))
```

type parameters:
- `TKey`: Type of key to compare items by.

##### `order_descending`
usage:
```py
assert one.source == (1, 2, 5, 4, 3)
assert one.order().source == (5, 4, 3, 2, 1)
```

##### `order_by_descending`
usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (Point(1, 2), Point(1, 3), Point(1, 1))
assert one.order_by(lambda point: point.y).source == (Point(1, 3), Point(1, 2), Point(1, 1))
```

type parameters:
- `TKey`: Type of key to compare items by.

#### `SupportsPrepend`

##### `prepend`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.prepend(0).source == (0, 1, 2, 3, 4, 5)
```

#### `SupportsReverse`

##### `reverse`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.reverse().source == (5, 4, 3, 2, 1)
```

#### `SupportsSelect`

type parameters:
- `TResult`: Type of result items.

##### `select`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (
    Point(0, 1),
    Point(0, 2),
    Point(0, 3),
    Point(0, 4),
    Point(0, 5)
)
assert one.select(lambda idx, point: (idx, point.y)).source == (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
)
```

##### `select_many`

usage:
```py
assert one.source == (
    Point(0, 1),
    Point(0, 2),
    Point(0, 3),
    Point(0, 4),
    Point(0, 5)
)
assert one.select_many(lambda _, point: (point.x, point.y)).source == (
    0,
    1,
    0,
    2,
    0,
    3,
    0,
    4,
    0,
    5
)
```

#### `SupportsSequenceEqual`

##### `sequence_equal`

usage:
```py
assert one.source == (1, 2, 3)
assert two.source == (3, 2, 1)
assert one.sequence_equal(two) is False
assert three.source == (1, 2, 3, 4)
assert one.sequence_equal(three) is False
assert four.source == (1, 2, 3)
assert one.sequence_equal(four) is True
```

#### `SupportsSingle`

##### `single`

usage:
```py
assert one.source == (7)
assert one.single() == 7
assert two.source == (1, 2, 3, 4, 5)
assert two.single(lambda x: x % 3 == 0) == 3
```

##### `single_or_default`

usage:
```py
assert one.source == (7)
assert one.single_or_default(5) == 7
assert two.source == (,)
assert two.single_or_default(5) == 5
assert three.source == (1, 2, 3, 4, 5)
assert three.single_or_default(0, lambda x: x % 7 == 0, ) == 0
assert four.source == (1, 2, 3, 4, 5)
assert four.single_or_default(0, lambda x: x % 2 == 0, ) == 0
assert five.source == (1, 2, 3, 4, 5)
assert five.single_or_default(0, lambda x: x % 5 == 0, ) == 5
```

#### `SupportsSkip`

##### `skip`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.skip(2).source == (3, 4, 5)
assert two.source == (1, 2, 3, 4, 5)
assert two.skip(2, 4).source == (1, 2, 5)
```

##### `skip_last`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.skip_last(2).source == (1, 2, 3)
```

##### `skip_while`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.skip_while(lambda idx, _: idx <= 3).source == (5,)
assert two.source == (1, 2, 3, 4, 5)
assert two.skip_while(lambda _, x: x <= 3).source == (4, 5)
```

#### `SupportsSum`

##### `sum`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.sum() == 15
```

#### `SupportsTake`

##### `take`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.take(2).source == (1, 2)
assert two.source == (1, 2, 3, 4, 5)
assert two.take(2, 4).source == (3, 4)
```

##### `take_last`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.take_last(2).source == (4, 5)
```

##### `take_while`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert one.take_while(lambda idx, _: idx <= 3).source == (1, 2, 3, 4)
assert two.source == (1, 2, 3, 4, 5)
assert two.take_while(lambda _, x: x <= 3).source == (1, 2, 3)
```

#### `SupportsUnion`

##### `union`

usage:
```py
assert one.source == (1, 2, 2, 3, 5)
assert two.source == (1, 3, 3, 4, 5)
assert one.union(two).source == (1, 2, 3, 5, 4)
```

##### `union_by`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (Point(0, 1), Point(0, 2), Point(0, 3))
assert two.source == (Point(1, 3), Point(1, 4), Point(1, 5))
assert one.union_by(two, lambda point: point.y).source == (
    Point(0, 1),
    Point(0, 2),
    Point(0, 3),
    Point(1, 4),
    Point(1, 4),
)
```

type parameters:
- `TKey`: Type of key to identify items by.

#### `SupportsWhere`

##### `where`

usage:
```py
Point = namedtuple('Point', ('x', 'y'))

assert one.source == (
    Point(0, 1),
    Point(2, 3),
    Point(4, 5),
    Point(6, 7),
)
assert one.where(lambda _, point: point.y <= 3).source == (
    Point(0, 1),
    Point(2, 3),
)
assert two.source == (
    Point(0, 1),
    Point(2, 3),
    Point(4, 5),
    Point(6, 7),
)
assert two.where(lambda idx, _: idx <= 2).source == (
    Point(0, 1),
    Point(2, 3),
    Point(4, 5),
)
```

#### `SupportsZip`

##### `zip`

usage:
```py
assert one.source == (1, 2, 3, 4, 5)
assert two.source == ("five", "four", "three")
assert one.zip(two).source == ((1, "five"), (2, "four"), (3, "three"))
```

type parameters:
- `TSecond`: Type of items of the second enumerable.

### Implementations

#### `PurePythonEnumerable`

Basic implementation of `pyenumerable.Enumerable`; Assumes that `TSource` conforms to `collections.abc.Hashable` & is immutable.<br/>
Violating this assumption may lead to unpredictable behaviour.

usage:
```py
from pyenumerable import pp_enumerable
my_enumerable = pp_enumerable(*items, from_iterable=from_iterable)
```

arguments:
- `items`: Directly used items
- `from_iterable`: An iterable of iterables which hold items
