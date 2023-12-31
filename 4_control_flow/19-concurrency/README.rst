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

Process, Threads in Python
--------------------------------

interpreter and thread
^^^^^^^^^^^^^^^^^^^^^^^

#. Python interpreter is a process. To run more processes:

        - multiprocessing
        - concurrent.futures
        - subprocess

#. Python interpreter uses single thread. to start more:
    
        - threading
        - concurrent.futures

GIL
^^^^^^^^

#. One python thread can hold the GIL and execute python code at a time.
    GIL control access to refrence count, and other interpreter states.

#. Python's bytecode interpreter interrupts threads periodically.
    OS scheduler can then pick other threads.

#. Built-in, Python/C APIs can release GIL.

#. Standard functions with syscalls releases the GIL: disk I/O, network I/O,
    time.sleep(). CPU-intensives in the NumPy/SciPy, zlib and bz2.

#. Python/C API level extensions can launch GIL-free threads.
    They can read write to the memory underlying objects that support the buffer
    protocol: bytearray, array.array, NumPy arrays.

Impact of GIL to different tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. The effect of the GIL on network programming with Python threads is
    relatively small, because the I/O functions release the GIL.

#. Contention over the GIL slows down compute-intensive Python threads.
    Sequential, single-threaded code is simpler and faster for such tasks.

#. To run CPU-intensive Python code on multiple cores, you must use
    multiple Python processes.
