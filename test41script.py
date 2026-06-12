import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Greeting program")
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--age', type=int, required=True)
    return parser.parse_args()


def main() -> None:

    print("Test: Beginning...\n")

    args = parse_args()
    print(f"Hello {args.name}, you are {args.age} years old.")

    print("\nTest: Ending....\n")


if __name__ == "__main__":
    main()
