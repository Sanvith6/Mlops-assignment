from pathlib import Path

import yaml


def load_config(path: str) -> dict:
    cfg_path = Path(path)
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    try:
        with open(cfg_path) as f:
            cfg = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid configuration file structure: {e}")

    if not isinstance(cfg, dict):
        raise ValueError("Invalid configuration file structure: expected key-value pairs.")

    for key in ("seed", "window", "version"):
        if key not in cfg:
            raise ValueError(f"Invalid configuration file structure: missing key '{key}'")

    return {
        "seed": int(cfg["seed"]),
        "window": int(cfg["window"]),
        "version": str(cfg["version"]),
    }
