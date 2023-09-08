- avoid blocking the event loop by delegating slow tasks to a
    different processing unit, from a simple thread all the way to a distributed task
    queue
- once you write your first async def, your program is inevitably going to have
     more and more async def, await, async with, and async for.
     And using non-asynchronous libraries suddenly becomes a challenge.
- asynchronous programming with native coroutines, DNS probing, awaitables,
    asynchronous context manager.
- asyncio.as_completed generator and the loop.run_in_executor coroutine
- a semaphore to limit the number of concurrent downloads
- Server-side asynchronous programming, asyncio and the TCP protocol.
- Asynchronous iteration and asynchronous iterables, async for, Python async console, 
    asynchronous generators, asynchronous generator expressions, and asynchronous
    comprehensions.
- Curio framework, structured concurrency
- main appeal of asynchronous programming, the misconception of “I/O-bound
    systems,” and dealing with the inevitable CPU-bound parts of your program.