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

Terminology
---------------

Concurrency:

    Run multiple tasks, and finish them, parallel or not.

Parallelism:

    Multiple computations at the same time.

Execution unit:

    Objects that execute concurrently, each with state and call stack.

    Python natively supports:

        - Process:

            Instance of a program.

            Communicate via pipes, sockets, files, in raw bytes.
            Object serialization is required.
            Allow preemptive multitasking.

        - Thread:

            Execution unit within a process.

            Communicate via shared memory.
            Allow preemptive multitasking.

        - Coroutine:

            Function that can be suspended and resumed.
            Allow cooperative multitasking.

Queue:

    Data sturcture that support put and get items, often in FIFO.
    Allow execution units to exchange data and messages.

Lock:

    An object that execution units uses to synchronize actions, avoid corruption.

Contention:

    Dispute over limite assets, such as lock, storage, CPU time.

