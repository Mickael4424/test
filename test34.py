import time

# 3.4


class Timer():
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.beg: float = 0.0
        self.end: float = 0.0

    def __enter__(self) -> "Timer":
        self.beg = time.time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.end = time.time()
        res = self.end - self.beg
        print(f"{self.name}: {res:.3f}s")


def main() -> None:

    print("Test: Beginning...\n")

    with Timer("mon operation"):
        time.sleep(0.5)

    print("\nTest: Ending....\n")


if __name__ == "__main__":
    main()
