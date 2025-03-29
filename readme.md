# PyEnumerable ![WTFPL License](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)

Implementation of .NET's [IEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1?view=net-9.0) interface in python W/ support for generics.

## Issue tracker
### v1.0.x
- [x] Design protocols for each operation set
- [x] Design & Implement `Enumerable` constructor(s) for PP implementation
- [x] Add pure python implementation of `Enumerable` (assuming inputs aren't guaranteed to be `Hashable` or immutable; preserving order)
    - [x] Any
    - [x] All
    - [x] Aggregate
    - [x] Chunk
    - [x] Average
    - [x] Append
    - [x] Except
    - [x] Distinct
    - [x] Count
    - [x] Contains
    - [x] Concat
    - [x] Join
    - [x] Intersect
    - [x] Group join
    - [x] Group by
    - [x] Prepend
    - [x] Order
    - [x] Min
    - [x] Skip
    - [x] Single
    - [x] Sequence equal
    - [x] Reverse
    - [x] Union
    - [x] Of type
    - [x] Take
    - [x] Sum
    - [x] Zip
    - [x] Where
    - [x] Select
    - [x] Max
- [x] remove `Comparable` bind from type variables
- [x] Publish on pypi
- [x] Add external constructor wrapper
- [x] Add technical documentation pure python implementation
- [x] Implement `__str__` & `__repr__` for 
### v1.1.x
- [ ] Improve test code quality
- [ ] Add hashed pure python implementation of `Enumerable` (assuming inputs are guaranteed to be `Hashable` & immutable; not preserving order)
