from contextlib import contextmanager
from typing import Generator
import time

# 3.41


@contextmanager
def timer(name: str) -> Generator:
    beg = time.time()
    yield
    elapsed = time.time() - beg
    print(f"{name}: {elapsed:.3f}s")


def main() -> None:

    print("\nTest: Beginning..\n")

    with timer("mon operation"):
        time.sleep(0.1)
        print("waiting")
        time.sleep(0.1)
        print("waiting")

    print("\nTest: Ending....\n")


if __name__ == "__main__":
    main()
