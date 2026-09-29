# Milestone 3 Supervisor Demonstration Guide

## Objective
Demonstrate the complete flow from synthetic personas to simulated survey/interview responses, validation, insights and product-use scoring.

## Recommended demo

```powershell
python main.py --test
python main.py --show-personas
python main.py --demo
```

The first repository contains five sample personas so the demonstration can start immediately. Generate the full set when required:

```powershell
python main.py --generate-personas 20
```

## Individual features

### Survey Mode
```powershell
python main.py --survey
```
Same questions are answered by all personas and displayed for comparison.

### Validation
```powershell
python main.py --validate
```
Checks consistency with persona characteristics and response realism.

### Interview Mode
```powershell
python main.py --interview
```
Select a persona and ask several related questions. The session keeps conversation history.

### Insight Extraction
```powershell
python main.py --insights
```
Produces recurring themes, sentiment, agreement/disagreement, behavioral trends, concerns and limitations.

## Supervisor explanation

**Survey Mode:** The same research questions are presented to multiple synthetic users so their simulated preferences can be compared.

**Persona consistency:** The system checks whether responses match defined characteristics such as price sensitivity, brand loyalty, technology adoption and review dependence.

**Interview Mode:** A selected persona answers multiple questions while the previous conversation is retained, allowing consistent multi-turn behavior.

**Insight Agent:** The collected responses are analyzed to find themes, sentiment patterns, agreement/disagreement and behavioral trends.

**Would-use score:** Every persona provides a 1–5 simulated willingness-to-use score with a reason. These are simulation results, not population estimates.

**Limitation:** Synthetic users are AI simulations and should be treated as hypotheses or research prototypes. Real-user validation is still required for empirical claims.
