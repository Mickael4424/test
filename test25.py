from pydantic import BaseModel, ValidationError


func_def = {
    "name": "fn_add_numbers",
    "description": "Add two numbers.",
    "parameters": {
        "a": {"type": "number"},
        "b": {"type": "number"}
    },
    "city": "Liverpool",
    "returns": {"type": "number"}
}


class ParameterDef(BaseModel):
    type: str


class FunctionDef(BaseModel):
    name: str
    description: str
    parameters: dict[str, ParameterDef]
    city: str
    returns: ParameterDef


def main() -> None:

    print("Test: Beginning...\n")

    try:
        fn = FunctionDef.model_validate(func_def)
        print(fn.name)
        print(fn.description)
        print(fn.returns.type)
        for cabbage, garden in fn.parameters.items():
            print(f"{cabbage}: {garden.type}")
    except ValidationError as e:
        print(f"Error: {e}")

    print("\nTest: Ending....\n")


if __name__ == "__main__":
    main()
