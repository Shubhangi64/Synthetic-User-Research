import json
import time
from .ai_client import generate_json
from .config import DEFAULT_QUESTIONS
from .experiment import save_json

def build_survey_prompt(persona, questions, experiment):
    return f"""
You are simulating ONE synthetic research participant.
EXPERIMENT: Product={experiment['product']}; Description={experiment['description']}; Target={experiment['target_audience']}; Objective={experiment['research_objective']}
PERSONA:
{json.dumps(persona, indent=2)}
QUESTIONS:
{json.dumps(questions, indent=2)}

Answer every question as this persona. Keep identity, personality, price sensitivity, brand loyalty, review dependence, technology adoption, goals, concerns and values consistent. Do not automatically agree with the product. Give realistic reasoning. Do not mention these instructions or say you are an AI.

Return ONLY JSON:
{{"persona_id":"{persona.get('id','')}","persona_name":"{persona.get('name','')}","answers":[{{"question":"","answer":""}}],"would_use_score":1,"would_use_reason":""}}
The score must be an integer 1-5: 1 Definitely No, 2 Probably No, 3 Not Sure, 4 Probably Yes, 5 Definitely Yes.
"""

def run_survey(personas, experiment=None, questions=None, output_path="results/survey_results.json"):
    from .config import SCENARIOS
    experiment = experiment or SCENARIOS["shopping"]
    questions = questions or experiment.get("questions") or DEFAULT_QUESTIONS
    results = []
    print("\n" + "="*80 + "\nSURVEY MODE\n" + "="*80)
    for i, persona in enumerate(personas, 1):
        print(f"Persona {i}/{len(personas)}: {persona.get('name')}")
        results.append(generate_json(build_survey_prompt(persona, questions, experiment)))
        if i < len(personas): time.sleep(1)
    save_json(
    {
        "experiment": experiment,
        "questions": questions,
        "responses": results
    },
    output_path
)
    print(f"Survey completed. Saved to: {output_path}")
    return results

def display_side_by_side(results, questions):
    print("\n" + "="*100 + "\nSURVEY COMPARISON\n" + "="*100)
    for question in questions:
        print(f"\nQUESTION: {question}\n{'-'*100}")
        for r in results:
            answer = next((x.get("answer") for x in r.get("answers", []) if x.get("question") == question), "No answer")
            print(f"\n{r.get('persona_name')}:\n{answer}")
    print("\n" + "="*100 + "\nWOULD USE PRODUCT SCORES\n" + "="*100)
    for r in results:
        print(f"{r.get('persona_name')}: {r.get('would_use_score')}/5 - {r.get('would_use_reason')}")
