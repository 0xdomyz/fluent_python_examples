from collections.abc import Generator
from typing import Union, NamedTuple


class Result(NamedTuple):  # <1>
    count: int  # type: ignore  # <2>
    average: float


class Sentinel:  # <3>
    def __repr__(self):
        return f"<Sentinel>"


STOP = Sentinel()  # <4>

# SendType = Union[float, Sentinel]  # <5>
SendType = float | Sentinel


def averager2(verbose: bool = False) -> Generator[None, SendType, Result]:
    # <1>, not yeilding, receive SendType, return Result
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield  # <2> receive only
        if verbose:
            print("received:", term)
        if isinstance(term, Sentinel):  # <3> return Result
            break
        total += term  # <4>
        count += 1
        average = total / count
    return Result(count, average)  # <5>


if __name__ == "__main__":
    # A coroutine to compute a running average.

    # Testing ``averager2`` by itself::

    coro_avg = averager2()
    next(coro_avg)  # prime the coroutine
    coro_avg.send(10)  # <1> yield None
    coro_avg.send(30)
    coro_avg.send(6.5)
    coro_avg.close()  # <2> raise exception at yield line, not return

    # Catching `StopIteration` to extract the value returned by
    # the coroutine::

    coro_avg = averager2()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        coro_avg.send(STOP)  # <1> return res, gen obj to raise StopIteration
    except StopIteration as exc:
        result = exc.value  # <2> value attr is the return value
    result  # <3>

    # Using `yield from` for delegating gen to get res of coro:

    def compute():
        # the yield from
        # machinery retrieves the return value when it handles the StopIteration
        # exception that marks the termination of the coroutine.
        res = yield from averager2(True)  # <1>
        print("computed:", res)  # <2>
        return res  # <3>

    comp = compute()  # <4> creat the coro obj

    for v in [None, 10, 20, 30, STOP]:  # <5>
        try:
            comp.send(v)  # <6>
        except StopIteration as exc:  # <7>
            result = exc.value

    result  # <8>
