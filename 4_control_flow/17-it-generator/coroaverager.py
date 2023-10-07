"""
A coroutine to compute a running average

# tag::CORO_AVERAGER_TEST[]
    >>> coro_avg = averager()  # <1>
    >>> next(coro_avg)  # <2> priming, starting and yielding initial value, altly, send(None) 
    0.0
    >>> coro_avg.send(10)  # <3>
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0

# end::CORO_AVERAGER_TEST[]
# tag::CORO_AVERAGER_TEST_CONT[]

    >>> coro_avg.send(20)  # <1>
    16.25

# <2> raises GeneratorExit exception, caught by generator, terminating the coroutine
    >>> coro_avg.close()
    >>> coro_avg.close()  # <3>
    >>> coro_avg.send(5)  # <4>
    Traceback (most recent call last):
      ...
    StopIteration

# end::CORO_AVERAGER_TEST_CONT[]

"""

# tag::CORO_AVERAGER[]
from collections.abc import Generator


def averager() -> Generator[float, float, None]:
    # returns
    # generator that yields float values, accepts float
    # values via .send(), and does not return a useful value
    total = 0.0
    count = 0
    average = 0.0
    while True:  # <2>
        term = yield average
        # <3>
        # suspends the coroutine, yields a result to the
        # client, and—later—gets a value sent by the caller to the coroutine
        total += term
        count += 1
        average = total / count


# end::CORO_AVERAGER[]
