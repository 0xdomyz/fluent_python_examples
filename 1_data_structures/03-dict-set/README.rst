- dic unpack, pattern matching, comp
- special mappings
- setdefault, update, |=
- The missing method lets you customize what happens when a key is not found.
- __missing__
- abc for mapping and mutable mapping, MappingProxyType
- dict_keys, dict_items


Running the tests
----------------------

Doctests::

    $ python3 -m doctest bisect_demo.py -v

Jupyter Notebook::

    #Install ``pytest`` and the ``nbval`` plugin:

    pip install pytest nbval

    pytest --nbval