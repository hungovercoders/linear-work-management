#!/usr/bin/env python3
"""Load the operating model (docs/model.yml), the one source of its facts."""
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODEL_FILE = ROOT / "docs" / "model.yml"


def load() -> dict:
    return yaml.safe_load(MODEL_FILE.read_text(encoding="utf-8"))


def expected_labels(model: dict) -> dict:
    """Label group -> set of values, or None for an open group."""
    out = {}
    for group, spec in model["labels"].items():
        values = spec["values"]
        out[group] = None if values == "open" else set(values)
    return out
