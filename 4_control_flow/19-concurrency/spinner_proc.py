# python3 spinner_proc.py

# Process: start(), join()
# Event: set(), wait()

# tag::SPINNER_PROC_IMPORTS[]
import itertools
import time
from multiprocessing import synchronize  # <2>

# Event is func that returns synchronize.Event
from multiprocessing import Event, Process  # <1>


def spin(msg: str, done: synchronize.Event) -> None:  # <3>
    # end::SPINNER_PROC_IMPORTS[]
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(0.1):
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


def slow() -> int:
    time.sleep(3)
    return 42


# tag::SPINNER_PROC_SUPER[]
def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=("thinking!", done))  # <4>
    print(f"spinner object: {spinner}")  # <5> shows proc id
    spinner.start()
    result = slow()
    done.set()
    # semophore: a signal that a process sends to another process
    spinner.join()
    return result


# end::SPINNER_PROC_SUPER[]


def main() -> None:
    result = supervisor()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
