from typing import Optional

# 3.2


def parse_int(value: str) -> Optional[int]:
    if value == "":
        print("Error: string empty")
        return None
    try:
        print(int(value))
        return int(value)
    except ValueError:
        print(f"Error: {value} is not a valid integer")
        return None
    except OverflowError:
        print(f"Error: {value} is too large")
        return None


def main() -> None:

    print("Test: Beginning...\n")

    parse_int("hello")
    parse_int("5")
    parse_int("5.6")
    parse_int("5" * 500)

    print("\nTest: Ending....\n")


if __name__ == "__main__":
    main()
