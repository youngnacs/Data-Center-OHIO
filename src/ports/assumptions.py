"""Load and validate campus planning assumptions."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ASSUMPTIONS = ROOT / "data" / "assumptions.yaml"


def load_assumptions(path: Path | None = None) -> dict[str, Any]:
    source = path or DEFAULT_ASSUMPTIONS
    with source.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("assumptions file must contain a mapping")
    required = ("program", "building_types", "phases", "campus_common", "power", "cooling")
    missing = [key for key in required if key not in data]
    if missing:
        raise ValueError(f"assumptions missing keys: {missing}")
    return data
