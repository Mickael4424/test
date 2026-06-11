from typing import Optional

# 3.1


def safe_divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        print("Error: cannot be divide by zero")
        return None
    else:
        return a/b


def main() -> None:

    print("Test: Beginning...\n")

    print(safe_divide(5.5, 0))
    print(safe_divide(10.0, 5.0))

    print("\nTest: Ending....\n")


if __name__ == "__main__":
    main()
