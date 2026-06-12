# python converter.py --input data.json               # output par défaut : output.json
# python converter.py --input data.json --output res.json
# python converter.py --input data.json --verbose     # flag booléen

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Greeting program")
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, default="output.json")
    parser.add_argument('--verbose', action='store_true')
    return parser.parse_args()


def main() -> None:

    print("Test: Beginning...\n")

    args = parse_args()
    print(f"File input: {args.input} // Output: {args.output} // Verbose: {args.verbose}")

    print("\nTest: Ending....\n")


if __name__ == "__main__":
    main()
