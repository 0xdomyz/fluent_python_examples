- Every Python object has an identity, a type, and a value, and only the value of an
     object may change over time.
- Immutable objects with equal values and immutable collections with ref to mut.
- Variables hold references' consequences:

    - simple assignment does not create copy
    - augmented assignment create new if bound to immutable
    - rebinding do not change object
    - function parameters passed as aliases
    - mutable para default open door to default being changed in place

- garbage collection
    - reference counting
    - cyclic garbage collection
- weak references
