import json

from .ai_client import generate_json
from .experiment import save_json
from .config import DATA_DIR


def validate_persona_responses(persona, survey_result):

    prompt = f"""
You are a Synthetic User Consistency and Realism Validation Agent.

PERSONA PROFILE:

{json.dumps(persona, indent=2)}

SURVEY RESPONSE:

{json.dumps(survey_result, indent=2)}

Check the following:

1. Identity consistency
2. Personality consistency
3. Price sensitivity
4. Brand loyalty
5. Review dependence
6. Technology adoption
7. Goals and values
8. Concerns
9. Contradictions
10. Overall realism

Important:
- Compare the survey response with the persona profile.
- Check whether the response matches the persona's stated characteristics.
- Identify contradictions.
- Do not invent problems if the response is reasonably consistent.

Return ONLY valid JSON using exactly this structure:

{{
    "persona_name": "",
    "persona_id": 0,
    "consistency_score": 1,
    "realism_score": 1,
    "status": "PASS",
    "issues": [],
    "explanation": ""
}}

Scores are from 1 to 5.

Use:
- PASS = reasonably consistent
- REVIEW = meaningful inconsistencies exist
"""


    result = generate_json(prompt)

    # Make sure persona information is preserved
    result["persona_name"] = persona.get(
        "name",
        result.get("persona_name", "Unknown")
    )

    result["persona_id"] = persona.get(
        "persona_id",
        result.get("persona_id")
    )

    return result


def run_validation(
    personas,
    survey_results,
    output_path=None
):
    """
    Validate survey responses against their corresponding personas.

    Matching is done using:
    1. persona_id
    2. persona name as fallback
    """

    if output_path is None:
        output_path = DATA_DIR / "validation_results.json"

    if isinstance(personas, dict):
        personas = [personas]

    if isinstance(survey_results, dict):
        survey_results = [survey_results]

    # ---------------------------------------------------------
    # Create lookup tables
    # ---------------------------------------------------------

    persona_id_map = {}
    persona_name_map = {}

    for index, persona in enumerate(personas, start=1):

        # Support the current persona_id system
        persona_id = persona.get("persona_id")

        # Fallback to position in the list
        if persona_id is None:
            persona_id = index
            persona["persona_id"] = index

        persona_id_map[str(persona_id)] = persona

        # Also create name-based lookup
        name = persona.get("name")

        if name:
            persona_name_map[
                name.strip().lower()
            ] = persona

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    results = []

    print("\n" + "=" * 80)
    print("PERSONA VALIDATION")
    print("=" * 80)

    for response in survey_results:

        response_id = response.get("persona_id")
        response_name = response.get("persona_name")

        persona = None

        # ---------------------------------------------
        # First try persona_id
        # ---------------------------------------------

        if response_id is not None:

            persona = persona_id_map.get(
                str(response_id)
            )

        # ---------------------------------------------
        # If ID fails, try persona name
        # ---------------------------------------------

        if persona is None and response_name:

            persona = persona_name_map.get(
                response_name.strip().lower()
            )

        # ---------------------------------------------
        # Persona not found
        # ---------------------------------------------

        if persona is None:

            print(
                f"Persona ID {response_id} not found."
            )

            results.append({
                "persona_name": response_name or "Unknown",
                "persona_id": response_id,
                "consistency_score": 0,
                "realism_score": 0,
                "status": "REVIEW",
                "issues": [
                    "Persona profile not found."
                ],
                "explanation": (
                    "The persona associated with this "
                    "survey response could not be found."
                )
            })

            continue

        # ---------------------------------------------
        # Validate
        # ---------------------------------------------

        print(
            f"Validating Persona "
            f"{persona.get('persona_id')}: "
            f"{persona.get('name')}"
        )

        result = validate_persona_responses(
            persona,
            response
        )

        results.append(result)

    # ---------------------------------------------------------
    # Save results
    # ---------------------------------------------------------

    save_json(
        {
            "validation_results": results
        },
        output_path
    )

    print(
        f"\nValidation saved to: "
        f"{output_path}"
    )

    return results

def print_validation_summary(results):

    print(
        "\n"
        + "=" * 80
        + "\nCONSISTENCY / REALISM VALIDATION\n"
        + "=" * 80
    )

    if not results:
        print("\nNo validation results found.")
        return

    for result in results:

        print(
            f"\nPersona {result.get('persona_id', '-')}: "
            f"{result.get('persona_name', 'Unknown')}"
        )

        print(
            f"Status: "
            f"{result.get('status', '-')}"
        )

        print(
            f"Consistency: "
            f"{result.get('consistency_score', '-')}/5"
        )

        print(
            f"Realism: "
            f"{result.get('realism_score', '-')}/5"
        )

        issues = result.get("issues", [])

        if issues:

            print("Issues:")

            for issue in issues:
                print(f"  - {issue}")

        else:

            print("Issues: None")

        explanation = result.get("explanation")

        if explanation:
            print(
                f"Explanation: {explanation}"
            )