- dynamic attributes, __getattr__, __new__
- the “bunch” idiom: using self.__dict__.update() to build
    arbitrary attributes from keyword arguments passed to __init__
- the Event class
- caching
- @functools.cached_property
- @property on top of @functools.cache
- property to protect
- property factory: closures, and instance attribute overriding
    by properties
- handling attribute deletion with properties
- the key special attributes, built-in functions, and
    special methods that support attribute metaprogramming