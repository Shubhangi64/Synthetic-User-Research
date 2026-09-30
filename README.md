# Generation of AI Powered Synthetic Users for Product Research

## 1. Project Overview

This project develops a **Synthetic User Generation Platform powered by Generative AI for product research**.

The goal is to create realistic AI-generated research participants with consistent demographic, personality, behavioral and preference characteristics. Researchers can then use these synthetic participants to explore product ideas, ask research questions, compare responses and extract early research insights.

> **Research limitation:** Synthetic users are AI simulations. Their outputs should be treated as simulated evidence/hypotheses and should not automatically be considered representative of real human populations.

---

# 2. Project Development From Milestone 2

This repository deliberately starts from **Milestone 2** and then continues into **Milestone 3**.

```text
MILESTONE 2
Foundation
   |
   +--> Experiment Workspace
   |
   +--> Persona Generation Agent
   |
   +--> Synthetic Personas
   |
   +--> Persona Memory / Consistency Foundation
   |
   v
MILESTONE 3
Research Simulation
   |
   +--> Survey Mode
   |
   +--> Consistency Validation
   |
   +--> Diverse Scenario Testing
   |
   +--> Interview Mode
   |
   +--> Insight Extraction
   |
   +--> Would-Use Scoring
   |
   +--> Insight Validation
```

Detailed milestone documentation:

- `MILESTONE_2.md`
- `MILESTONE_3.md`
- `PROJECT_ROADMAP.md`

---

# 3. Current Experiment

## Product

**AI Personal Shopping Platform**

## Target Audience

**Online shoppers aged 18–40**

## Research Objective

> To understand the preferences, expectations, concerns, and behavioral responses of online shoppers toward an AI-powered personal shopping platform.

## Product Features

- AI product recommendations
- Price comparison
- Personalized shopping feed
- Review summarization
- Virtual try-on
- Price-drop alerts
- Budget-based shopping
- Brand comparison
- Alternative product suggestions
- Return-policy comparison
- AI shopping assistant

The formal experiment definition is stored in `data/experiment.json`.

---

# 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Gemini API | Generative AI for personas and research responses |
| `google-genai` | Gemini Python SDK |
| `python-dotenv` | API key configuration |
| JSON | Lightweight data and result storage |
| VS Code | Local development |
| Git | Version control |
| GitHub | Project repository |

### Intentionally not used

- SQLite
- FastAPI
- Separate database server
- Complex backend framework

This keeps the academic prototype simple and easy to demonstrate.

---

# 5. Repository Structure

```text
synthetic-user-research/
│
├── README.md
├── MILESTONE_2.md
├── MILESTONE_3.md
├── PROJECT_ROADMAP.md
├── MILESTONE_3_GUIDE.md
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│   ├── experiment.json
│   └── personas.json
│
├── results/
│   └── .gitkeep
│
└── src/
    ├── __init__.py
    ├── config.py
    ├── ai_client.py
    ├── experiment.py
    ├── personas.py
    ├── survey.py
    ├── interview.py
    ├── validation.py
    └── insights.py
```

---

# 6. Milestone 2 — Foundation

## 6.1 Study of Synthetic User Research

The project studies how Generative AI can simulate research participants using structured persona profiles and controlled prompts.

The system does not simply generate a name and description. Each persona contains behavioral attributes that are reused during subsequent interactions.

## 6.2 System Architecture

```text
Experiment Workspace
        |
        v
Persona Generation Agent
        |
        v
Synthetic Persona Profiles
        |
        v
Persona Memory / Consistency
        |
        v
Multi-turn Persona Interaction
```

## 6.3 Experiment Workspace

The experiment contains:

- Product
- Product description
- Target audience
- Research objective
- Product features
- Research questions

## 6.4 Persona Generation Agent

Each persona contains:

- Name
- Age
- Occupation
- Location
- Income
- Personality traits
- Communication style
- Decision-making style
- Shopping frequency
- Price sensitivity
- Brand loyalty
- Review dependence
- Technology adoption
- Impulse buying
- Goals
- Motivations
- Pain points
- Concerns
- Values
- Preferred categories
- Preferred brands
- Budget preference
- Important product factors
- Profile summary

## 6.5 Persona Memory

The interview module keeps conversation history in memory for the current session and supplies the persona profile and previous conversation to the model for each new turn.

No database is required for this prototype.

---

# 7. Milestone 3 — Research Simulation

## 7.1 Survey Mode

The same research questions are sent to multiple personas.

Example:

```text
Question 1: What do you think about AI shopping recommendations?
Question 2: Would you trust AI for expensive purchases?
Question 3: Which feature would be most useful?
Question 4: What is your biggest concern?
Question 5: Would you use this product? Give a score from 1–5.
```

Responses are stored and displayed for comparison.

## 7.2 Consistency and Realism Validation

The validation agent checks whether generated answers agree with the persona profile.

Examples:

- High price sensitivity should generally correspond to concern about price/value.
- High review dependence should generally correspond to checking reviews.
- Low technology adoption should generally correspond to more cautious AI use.
- Privacy-conscious personas should generally show stronger privacy concerns.

The validation produces consistency and realism scores plus identified issues.

## 7.3 Diverse Experiment Scenarios

Three sample scenarios are included in `src/config.py`:

- AI Personal Shopping Platform
- AI Fitness and Workout Platform
- AI Online Grocery Shopping Platform

Run a scenario with:

```powershell
python main.py --survey --scenario shopping
python main.py --survey --scenario fitness
python main.py --survey --scenario grocery
```

## 7.4 Interview Mode

A researcher can select one persona and ask multiple questions.

The persona maintains the session history and uses its original profile when answering later questions.

Run:

```powershell
python main.py --interview
```

## 7.5 Insight Extraction Agent

The agent analyzes survey and interview responses and extracts:

- Recurring themes
- Sentiment breakdown
- Agreement patterns
- Disagreement patterns
- Behavioral trends
- Feature preferences
- Concerns
- Segment observations
- Research implications
- Limitations

Run:

```powershell
python main.py --insights
```

## 7.6 Would-Use Product Score

Each persona provides a structured 1–5 score:

```text
1 = Definitely No
2 = Probably No
3 = Not Sure
4 = Probably Yes
5 = Definitely Yes
```

The system calculates the aggregate average and score distribution while preserving each persona's reasoning.

These are **synthetic experiment results**, not predictions about the actual market.

## 7.7 Insight Validation

The system can be tested with different product scenarios to check whether the extracted themes remain relevant to the responses and whether persona differences are reflected in the results.

---

# 8. Windows + VS Code Setup

## Step 1 — Open the project

Open the `synthetic-user-research` folder in VS Code.

## Step 2 — Create a virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again.

## Step 3 — Install packages

```powershell
pip install -r requirements.txt
```

## Step 4 — Create `.env`

Copy `.env.example` to `.env` and enter your Gemini API key:

```env
GEMINI_API_KEY=YOUR_REAL_GEMINI_API_KEY
GEMINI_MODEL=gemini-3.5-flash-lite
```

**Never commit `.env` or expose the API key on GitHub.**

---

# 9. Run Milestone 2 First

This is the recommended demonstration sequence.

### Test Gemini

```powershell
python main.py --test
```

### Generate the persona population

```powershell
python main.py --generate-personas 20
```

If five personas already exist, the program generates only the missing personas.

### Display personas

```powershell
python main.py --show-personas
```

At this point, Milestone 2 has produced the synthetic-user foundation required by Milestone 3.

---

# 10. Run Milestone 3

## Survey

```powershell
python main.py --survey
```

## Validation

```powershell
python main.py --validate
```

## Interview

```powershell
python main.py --interview
```

## Insights

```powershell
python main.py --insights
```

## Complete demonstration

```powershell
python main.py --demo
```

The demo intentionally uses five personas to reduce API usage. The full survey can be run using all available personas.

---

# 11. Output Files

After running experiments:

```text
results/
├── survey_results.json
├── validation_results.json
├── interview_results.json
└── insights.json
```

These files provide evidence that the individual Milestone 3 modules executed successfully.

---

# 12. GitHub Setup

Create a GitHub repository named:

```text
synthetic-user-research
```

From the VS Code terminal:

```powershell
git init
git add .
git commit -m "Start project from Milestone 2 foundation"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/synthetic-user-research.git
git push -u origin main
```

After completing Milestone 3:

```powershell
git add .
git commit -m "Implement Milestone 3 research simulation"
git push
```

Recommended development commits:

```text
Start project from Milestone 2 foundation
Add experiment workspace
Add Gemini API integration
Add persona generation agent
Add synthetic persona dataset
Add persona memory foundation
Add Survey Mode
Add consistency validation
Add diverse experiment scenarios
Add Interview Mode
Add Insight Extraction Agent
Add Would-Use scoring
Add Milestone 3 validation
Update project documentation
```

---



# 13. Final Project Flow

```text
Researcher
    |
    v
Experiment Workspace
    |
    +--> Product
    +--> Target Audience
    +--> Research Objective
    +--> Questions
    |
    v
Persona Generation Agent
    |
    v
Synthetic User Population
    |
    +-------------------+
    |                   |
    v                   v
Survey Mode        Interview Mode
    |                   |
    +---------+---------+
              |
              v
       Response Dataset
              |
              v
    Consistency Validation
              |
              v
      Insight Extraction
              |
       +------+------+-------+
       |      |      |       |
       v      v      v       v
    Themes Sentiment Agreement Trends
              |
              v
     Would-Use Product Score
              |
              v
       Research Insights
```

---
