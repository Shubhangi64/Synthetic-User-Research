# Milestone 3 — Research Simulation and Insight Extraction

## Objective
Use the synthetic personas created in Milestone 2 to perform product research experiments and extract structured insights.

## Components

1. Survey Mode — same questions to all personas and side-by-side comparison.
2. Persona consistency and response realism validation.
3. Testing across diverse personas and product scenarios.
4. Interview Mode — multi-turn conversation with memory and persona consistency.
5. Insight Extraction Agent — themes, sentiment, agreement/disagreement and behavioral trends.
6. "Would use this product?" scoring from 1–5 with reasoning.
7. Validation of insight quality across experiment scenarios.

## Commands

Survey:

```powershell
python main.py --survey
```

Interview:

```powershell
python main.py --interview
```

Consistency validation:

```powershell
python main.py --validate
```

Insight extraction:

```powershell
python main.py --insights
```

Complete demonstration:

```powershell
python main.py --demo
```

## Output files

The system creates:

```text
results/survey_results.json
results/validation_results.json
results/interview_results.json
results/insights.json
```

## Research interpretation

These results are synthetic simulations. They should be used for hypothesis generation, scenario testing and early product research, not as automatic evidence that represents the real population.
