import json

from .ai_client import generate_json
from .experiment import save_json


def calculate_scores(survey_results):

    scores = [
        r.get("would_use_score")
        for r in survey_results
        if isinstance(r.get("would_use_score"), int)
        and 1 <= r.get("would_use_score") <= 5
    ]

    return {
        "count": len(scores),
        "average": round(sum(scores) / len(scores), 2) if scores else None,
        "distribution": {
            str(i): scores.count(i)
            for i in range(1, 6)
        }
    }


def extract_insights(experiment, survey_results, interview=None):

    prompt = f"""
You are an Insight Extraction Agent for synthetic product research.

EXPERIMENT:

{json.dumps(experiment, indent=2)}

SURVEY RESPONSES:

{json.dumps(survey_results, indent=2)}

INTERVIEW:

{json.dumps(interview or {}, indent=2)}

Analyze only the evidence provided.

Identify:
- recurring themes
- positive, neutral and negative sentiment patterns
- agreement patterns
- disagreement patterns
- behavioral trends
- feature preferences
- concerns
- segment observations
- research implications
- limitations of synthetic evidence

Do not invent information that is not present in the provided evidence.

Return ONLY valid JSON:

{{
    "summary": "",
    "recurring_themes": [
        {{
            "theme": "",
            "evidence": "",
            "affected_personas": []
        }}
    ],
    "sentiment_breakdown": {{
        "positive": 0,
        "neutral": 0,
        "negative": 0
    }},
    "agreement_patterns": [],
    "disagreement_patterns": [],
    "behavioral_trends": [],
    "feature_preferences": [],
    "concerns": [],
    "segment_observations": [],
    "research_implications": [],
    "limitations": []
}}

Sentiment percentages should approximately sum to 100.
"""

    return generate_json(prompt)


def build_final_analysis(experiment, survey_results, interview=None):

    final = {
        "experiment": experiment,
        "would_use_product": calculate_scores(survey_results),
        "insights": extract_insights(
            experiment,
            survey_results,
            interview
        )
    }

    # save_json expects:
    # save_json(data, file_path)
    save_json(
        final,
        "results/insights.json"
    )

    return final


def print_insights(final):

    i = final["insights"]

    print(
        "\n"
        + "=" * 80
        + "\nINSIGHT EXTRACTION RESULTS\n"
        + "=" * 80
    )

    print("\nSUMMARY")
    print(i.get("summary"))

    print("\nWOULD USE PRODUCT")
    print(final["would_use_product"])

    print("\nRECURRING THEMES")

    for x in i.get("recurring_themes", []):
        print(
            f"- {x.get('theme')}: "
            f"{x.get('evidence')}"
        )

    print("\nSENTIMENT")
    print(
        json.dumps(
            i.get("sentiment_breakdown", {}),
            indent=2
        )
    )

    print("\nAGREEMENT PATTERNS")

    for x in i.get("agreement_patterns", []):
        print("-", x)

    print("\nDISAGREEMENT PATTERNS")

    for x in i.get("disagreement_patterns", []):
        print("-", x)

    print("\nBEHAVIORAL TRENDS")

    for x in i.get("behavioral_trends", []):
        print("-", x)

    print("\nLIMITATIONS")

    for x in i.get("limitations", []):
        print("-", x)
