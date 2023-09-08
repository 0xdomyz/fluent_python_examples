- concurrent.futures.Future, asyncio.Future
- Executor.submit, concurrent.futures.as_completed.
- concurrent.futures.ProcessPoolExecutor to go around the GIL and use multiple CPU cores
- concurrent.futures.ThreadPoolExecutor
- progress bar and proper error handling future.as_completed generator function
- storing futures in a dict to link further information to them when submitting
    so that we can use that information when the future comes out of the
    as_completed iterator.