"""
3 main way to run coroutines
------------------------------
#. asyncio.run(coro):

    call from func, to drive entry point coroutine.
    block.

#. asyncio.create_task(coro)

    call from coro to schedule another coroutine.
    not block, return Task object for control.

#. await coro

    call from coro to transfer control to another coroutine.
    suspend current coroutine.

"""
# python3 spinner_async.py

# asyncio: run(), create_task(), sleep()
# await: async def, asyncio.sleep()
# Task: cancel(), asyncio.CancelledError


# tag::SPINNER_ASYNC_TOP[]
import asyncio
import itertools


async def spin(msg: str) -> None:  # <1> no need event
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(0.1)  # <2> pause without blocking other coro
        except asyncio.CancelledError:  # <3>
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


async def slow() -> int:
    await asyncio.sleep(3)  # <4> yield control to event loop, which runs other coro
    return 42


# end::SPINNER_ASYNC_TOP[]


# tag::SPINNER_ASYNC_START[]
def main() -> None:  # <1> func, not coroutine
    result = asyncio.run(supervisor())  # <2> start event loop, block
    print(f"Answer: {result}")


async def supervisor() -> int:  # <3> native coroutine
    spinner: asyncio.Task = asyncio.create_task(spin("thinking!"))  # <4> schedule
    print(f"spinner object: {spinner}")  # <5>
    result = await slow()  # <6> call coroutine, block
    spinner.cancel()  # <7> raise CancelledError in coroutine
    return result


if __name__ == "__main__":
    main()
# end::SPINNER_ASYNC_START[]
