class A:
    def __repr__(self):
        return "repr"


a = A()

# for developer
a

# for end user
str(a)  # str() calls __str__ if it exists, otherwise __repr__
print(a)  # print uses str()


class B:
    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"


b = B()

# for developer
b

# for end user
str(b)
print(b)
