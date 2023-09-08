- use special methods and conventions to get pythonic objects
- simple is better than complex

    - if for app, focus on what is needed to support end user
    - if for lib, have special methods to support pythonic idioms

- frombytes, @classmethod, @staticmethod
- format specification mini language, __format__
- __hash__, xor, immutable, private attribute
- __slots__
- overriding class attribute accessed via instance, self.typecode

Notes
----------

The _memtest.py_ script takes a module name in the command line and loads it.
Assuming the module defines a class named `Vector`, _memtest.py_ creates a list with 10 million instances, reporting the memory usage before and after the list is created.
