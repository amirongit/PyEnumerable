# PyEnumerable ![WTFPL License](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)

Implementation of .NET's [IEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1?view=net-9.0) interface in python W/ support for generics.

## Architecture & Design

PyEnumerable follows a relatively simple architecture, mainly because there isn't any reason to do otherwise!
Extension methods defined by `IEnumerable` interface are grouped by their functionality under protocols located `pyenumerable.protocol` package; The main advantage provided by protocols over ABCs (abstract base classes) is the ability to define overloads w/ different signatures.

### Protocols

#### Common Type Variables Among Protocols

##### `TSource`

Type of the items inside an instance of a particular implementation of `Enumerable`.

#### Common Arguments Among Methods

##### `comparer`

A callable which accepts two arguments of type `Tsource` & returns a `bool` value; The meaning of the returned value is dependant on the context of its method; usually defaults to `lambda i, o: i == o`.

#### `Enumerable`

This protocol consolidates all other protocols into a single one, allowing implementations to reference it instead of listing each individual protocol. This approach minimizes the risk of omitting any methods due to oversight.
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
