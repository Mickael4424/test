from typing import Optional
import json

# 3.3


def read_json_file(path: str) -> Optional[dict]:
    try:
        with open(path, 'r') as fichier:
            data = json.load(fichier)
            print(data)
            return data
    except FileNotFoundError:
        print(f"File not found {path}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON invalid {e} {path}")
        return None


def main() -> None:

    print("Test: Beginning...\n")

    path = "test.json"
    read_json_file(path)

    path = "valid.json"
    read_json_file(path)

    path = "invalid.json"
    read_json_file(path)
    print("\nTest: Ending....\n")


if __name__ == "__main__":
    main()
