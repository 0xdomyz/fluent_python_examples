Concurrency methods

- Threads, with the threading package
- Processes, with multiprocessing
- Asynchronous coroutines with asyncio

GIL

- CPU-intensive functions must be avoided in asyncio, as they block the event loop.
- Python periodically interrupts threads
- The multiprocessing variant worked around the GIL

- only processes allow Python to benefit from multicore CPUs
- Python’s GIL makes threads worse than sequential code for heavy computations

- the GIL doesn’t affect many use cases of Python in system administration
- worked around the GIL with industrial-strength solutions
- WSGI application servers
- distributed task queues