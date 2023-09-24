# example1
class A:
    def __repr__(self):
        return "repr"


a = A()

a  # for developer
# for end user
str(a)  # str() calls __str__ if it exists, otherwise __repr__
print(a)  # print uses str()


# example 2
class B:
    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"


b = B()
b
str(b)
print(b)

# example 3
from collections import namedtuple

a = namedtuple("Point", "x y")(1, "two")
a
repr(a)
str(a)
print(a)

# namd tuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)

print(repr(p))
print(str(p))

p.__str__()  # not helpful

# dict
d = {"a": 1, "b": "two"}
repr(d)
str(d)

# dataframe
import pandas as pd

df = pd.DataFrame({"a": [1, 2], "b": ["two", "three"]})
repr(df)
str(df)

large_df = pd.DataFrame({"a": range(1000), "b": range(1000)})
repr(large_df)
str(large_df)

# datetime
import datetime

today = datetime.datetime.now()
repr(today)
str(today)
