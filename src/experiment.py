import json
from pathlib import Path

from .config import DATA_DIR, SCENARIOS


def save_json(data, file_path):
    """Save Python data to a JSON file."""

    file_path = Path(file_path)

    # Create parent folder if it does not exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def load_json(file_path, default=None):
    """Load JSON data from a file."""

    file_path = Path(file_path)

    if not file_path.exists():
        if default is not None:
            return default
        return {}

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_personas():
    """
    Load generated personas if available.
    Otherwise load the original sample personas.

    Persona IDs are reset to:
    1, 2, 3, ... N
    """

    generated_file = DATA_DIR / "personas_generated.json"
    original_file = DATA_DIR / "personas.json"

    if generated_file.exists():

        personas = load_json(
            generated_file,
            []
        )

        print(f"Loading personas from: {generated_file}")

    elif original_file.exists():

        personas = load_json(
            original_file,
            []
        )

        print(f"Loading personas from: {original_file}")

    else:

        personas = []

    # Make sure IDs are 1, 2, 3, ... N
    for i, persona in enumerate(personas, start=1):

        persona["persona_id"] = i

        # Remove old UUID ID if present
        if "id" in persona:
            del persona["id"]

    return personas


def save_personas(personas, generated=True):
    """
    Save personas with sequential IDs.
    """

    # Assign sequential IDs
    for i, persona in enumerate(personas, start=1):

        persona["persona_id"] = i

        if "id" in persona:
            del persona["id"]

    if generated:

        file_path = DATA_DIR / "personas_generated.json"

    else:

        file_path = DATA_DIR / "personas.json"

    save_json(
        personas,
        file_path
    )

    return file_path


def get_scenario(name):
    """
    Return a predefined experiment scenario.
    """

    if name not in SCENARIOS:

        available = ", ".join(
            SCENARIOS.keys()
        )

        raise ValueError(
            f"Unknown scenario '{name}'. "
            f"Available scenarios: {available}"
        )

    return SCENARIOS[name]