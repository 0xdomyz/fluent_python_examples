#!/usr/bin/env python3.11
import time
from clockdeco import clock


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock
def add(a=0, b=0):
    return a + b


if __name__ == "__main__":
    print("*" * 40, "Calling snooze(.123)")
    snooze(0.123)
    print("*" * 40, "Calling factorial(6)")
    print("6! =", factorial(6))
    print("*" * 40, "Calling add(a=1, b=2)")
    print("1 + 2 =", add(a=1, b=2))
    print("name of snooze:", snooze.__name__)
