from pydantic import BaseModel, ValidationError
import json


class ParameterDef(BaseModel):
    type: str


class FunctionDef(BaseModel):
    name: str
    description: str
    parameters: dict[str, ParameterDef]
    returns: ParameterDef


def load_function_definitions(path: str) -> list[FunctionDef]:
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in {path} : {e}")
        return []
    if not isinstance(data, list):
        print(f"Error: expected a list in {path}")
        return []
    result: list[FunctionDef] = []
    for item in data:
        try:
            result.append(FunctionDef.model_validate(item))
        except ValidationError as e:
            print(f"Error: skipping invalid entry {e}")
    print(f"Loaded: {len(result)} function(s)")
    return result


def main() -> None:

    print("Test: Beginning...\n")

    load_function_definitions("absent.json")
    load_function_definitions("invalid.json")
    load_function_definitions("notalist.json")
    load_function_definitions("functions_definition.json")

    print("\nTest: Ending....\n")


if __name__ == "__main__":
    main()
