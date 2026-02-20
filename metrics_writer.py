import json


def write_metrics(path: str, payload: dict) -> None:
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print(json.dumps(payload, indent=2))
