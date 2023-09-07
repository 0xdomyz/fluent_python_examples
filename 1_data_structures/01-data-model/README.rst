- special methods enables objects to behave like built-in types
- __repr__ is for developers
- __str__ is for end users
- Emulating sequences
- numeric types

Doctests::

    python3 -m doctest frenchdeck.doctest -v

    # And to check doctests embedded in a module:

    python3 -m doctest vector2d.py -v

Jupyter Notebook::

    #Install ``pytest`` and the ``nbval`` plugin:

    pip install pytest nbval

    pytest --nbval
