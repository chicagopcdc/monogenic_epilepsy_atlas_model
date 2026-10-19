"""Data model package for monogenic-epilepsy-atlas-schema."""

from pathlib import Path
from .monogenic_epilepsy_atlas_schema import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "monogenic_epilepsy_atlas_schema.yaml"
