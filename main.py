import argparse, json, sys
from src.ai_client import test_connection
from src.config import SCENARIOS
from src.experiment import load_personas, get_scenario
from src.personas import generate_to_target, print_personas
from src.survey import run_survey, display_side_by_side
from src.validation import run_validation, print_validation_summary
from src.interview import run_interactive_interview
from src.insights import build_final_analysis, print_insights

def load_or_fail():
    personas=load_personas()
    if not personas:
        print("No personas found. Run: python main.py --generate-personas 20")
        sys.exit(1)
    return personas

def run_demo():
    print("\n"+"="*80+"\nMILESTONE 3 DEMONSTRATION\n"+"="*80)
    personas=load_personas()
    if len(personas)<5:
        print("At least 5 personas are required. Run: python main.py --generate-personas 20"); return
    demo_personas=personas[:5]
    experiment=get_scenario("shopping")
    print("Using 5 personas for demo; full system supports all 20.")
    survey=run_survey(demo_personas,experiment=experiment)
    display_side_by_side(survey,experiment["questions"])
    validation=run_validation(demo_personas,survey)
    print_validation_summary(validation)
    final=build_final_analysis(experiment,survey)
    print_insights(final)
    print("\nDemo complete. See results/.")

def main():
    parser=argparse.ArgumentParser(description="Synthetic User Research Platform - Milestone 3")
    parser.add_argument("--test",action="store_true")
    parser.add_argument("--generate-personas",type=int,metavar="N")
    parser.add_argument("--show-personas",action="store_true")
    parser.add_argument("--survey",action="store_true")
    parser.add_argument("--interview",action="store_true")
    parser.add_argument("--validate",action="store_true")
    parser.add_argument("--insights",action="store_true")
    parser.add_argument("--demo",action="store_true")
    parser.add_argument("--scenario",choices=list(SCENARIOS.keys()),default="shopping")
    args=parser.parse_args()
    if args.test:
        try: print("Gemini connection test successful." if test_connection() else "Unexpected response.")
        except Exception as e: print(f"Connection test failed: {e}")
        return
    if args.generate_personas:
        print_personas(generate_to_target(args.generate_personas)); return
    if args.show_personas:
        print_personas(load_or_fail()); return
    if args.survey:
        p=load_or_fail(); e=get_scenario(args.scenario); r=run_survey(p,e); display_side_by_side(r,e["questions"]); return
    if args.interview:
        run_interactive_interview(load_or_fail(),get_scenario(args.scenario)); return
    if args.validate:
        p=load_or_fail()

        try:
            with open("results/survey_results.json",encoding="utf-8") as f:
                saved=json.load(f)
        except FileNotFoundError:
            print("Run --survey first.")
            return

        print_validation_summary(
            run_validation(p,saved["responses"])
        )
        return
    if args.insights:
        try:
            with open("results/survey_results.json",encoding="utf-8") as f: saved=json.load(f)
        except FileNotFoundError:
            print("Run --survey first."); return
        print_insights(build_final_analysis(saved["experiment"],saved["responses"])); return
    if args.demo: run_demo(); return
    parser.print_help()

if __name__ == "__main__": main()
