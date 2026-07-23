"""Runtime configuration loading for the fetcher service."""

import json
from pathlib import Path

DEFAULTS = {"timeout_seconds": 30, "retries": 3}


def load_config(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    unknown = set(data) - set(DEFAULTS)
    if unknown:
        raise ValueError(f"unknown config keys: {sorted(unknown)}")
    config = dict(DEFAULTS)
    config.update(data)
    return config
