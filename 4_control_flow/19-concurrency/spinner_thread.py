# python3 spinner_thread.py

# Thread obj: start(), join()
# Event obj: set(), wait()

# tag::SPINNER_THREAD_TOP[]
import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:  # done is obj to sync threads
    for char in itertools.cycle(r"\|/-"):  # infinite loop
        status = f"\r{char} {msg}"  # <3> carriage return to animate
        print(status, end="", flush=True)  # flush=True to force print
        # print("a\rb")
        # print("aaa", end="") # no newline
        if done.wait(0.1):  # <4>
            # An Event instance has an internal boolean flag that starts
            # as False. Calling Event.set() sets the flag to True. While the flag is
            # false, if a thread calls Event.wait(), it is blocked until another thread
            # calls
            # Event.set(), at which time Event.wait() returns True. If a timeout in
            # seconds is given to Event.wait(s), this call returns False when the
            # timeout elapses, or returns True as soon as Event.set() is called by
            # another thread.
            break  # <5>
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")  # <6> clear line


def slow() -> int:
    time.sleep(3)  # <7> block main thread, but GIL released
    return 42


# end::SPINNER_THREAD_TOP[]


# tag::SPINNER_THREAD_REST[]
def supervisor() -> int:  # <1>
    done = Event()  # <2> coordination object
    spinner = Thread(target=spin, args=("thinking!", done))  # <3> invoke callable
    print(f"spinner object: {spinner}")  # <4>
    # shows that the thread is not running yet
    spinner.start()  # <5>
    result = slow()  # <6> block main thread, but GIL released, spinner runs
    done.set()  # <7> signal to spinner to stop
    spinner.join()  # <8> wait for spinner thread to finish
    return result


def main() -> None:
    result = supervisor()  # <9>
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
# end::SPINNER_THREAD_REST[]
