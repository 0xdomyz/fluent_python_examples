"""
Python code using asyncio has
only one flow of execution, unless you’ve explicitly started additional threads
or processes. That means only one coroutine executes at any point in time.
Concurrency is achieved by control passing from one coroutine to another.
"""

# python3 spinner_async_experiment.py


import asyncio
import itertools
import time


async def spin(msg: str) -> None:
    print("THIS WILL NEVER BE OUTPUT")
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    print("THIS WILL NEVER BE OUTPUT")


# tag::SPINNER_ASYNC_EXPERIMENT[]
async def slow() -> int:
    time.sleep(3)  # <4> blocks the thread
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin("thinking!"))  # <1>
    print(f"spinner object: {spinner}")  # <2> shows pending task
    result = await slow()  # <3> transfer control to slow()
    spinner.cancel()  # <5> control never reache body of spin()
    return result


# end::SPINNER_ASYNC_EXPERIMENT[]


def main() -> None:
    result = asyncio.run(supervisor())
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
