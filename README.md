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

# 13. Supervisor Demonstration

Use this sequence during the meeting:

### Part A — Explain the problem

Real user research can require time, money and participant recruitment. This project explores whether LLM-generated synthetic users can support early product research and hypothesis generation.

### Part B — Show Milestone 2

Open:

```text
data/experiment.json
```

Then show:

```text
data/personas.json
```

Explain how the experiment definition becomes the input to persona generation.

### Part C — Show persona diversity

Use:

```powershell
python main.py --show-personas
```

Explain differences in personality, price sensitivity, technology adoption, brand loyalty and review dependence.

### Part D — Show Survey Mode

```powershell
python main.py --survey
```

Explain that every persona receives the same research questions.

### Part E — Show consistency validation

```powershell
python main.py --validate
```

Explain that the generated responses are checked against the persona profile.

### Part F — Show Interview Mode

```powershell
python main.py --interview
```

Ask related questions and demonstrate that the persona retains the current conversation.

### Part G — Show Insight Extraction

```powershell
python main.py --insights
```

Explain themes, sentiment, agreement, disagreement and behavioral trends.

### Part H — Show Would-Use Score

Explain the 1–5 score and the reasoning stored for each persona.

### Part I — Show GitHub

Open the GitHub repository and show:

- README
- milestone documents
- source code
- data
- generated result files when appropriate
- commit history

---

# 14. Viva Questions

### Why use synthetic users?

They allow controlled early-stage simulation of different user profiles without requiring participants for every exploratory experiment.

### How are personas made different?

The generation prompt provides the existing persona summaries and asks the model to vary demographic, behavioral and psychological attributes.

### How is consistency maintained?

The persona profile and conversation history are supplied during subsequent interactions, and a separate validation step checks whether responses remain aligned with the profile.

### Why is JSON used?

The project is an academic prototype and JSON provides simple persistent storage without introducing a database.

### Why are SQLite and FastAPI not used?

They are not necessary for the current prototype. The focus is the synthetic-user research workflow rather than a production web API.

### What does Survey Mode do?

It asks the same questions to multiple synthetic personas and stores their responses for comparison.

### What does Interview Mode do?

It provides a multi-turn conversation with one selected persona while retaining the current session history.

### What does the Insight Agent do?

It analyzes collected responses and identifies themes, sentiment, agreement/disagreement, behavioral trends and segment observations.

### Can these results be treated as real customer data?

No. They are simulated outputs. Real-user research is still required for empirical validation.

---

# 15. Current Completion Status

| Milestone | Component | Status |
|---|---|---|
| M2 | Synthetic user research foundation | Completed |
| M2 | System architecture | Completed |
| M2 | Experiment workspace | Completed |
| M2 | Persona Generation Agent | Completed |
| M2 | Persona data model | Completed |
| M2 | Persona memory foundation | Completed |
| M3 | Survey Mode | Implemented |
| M3 | Consistency validation | Implemented |
| M3 | Diverse scenario testing | Implemented |
| M3 | Interview Mode | Implemented |
| M3 | Insight Extraction Agent | Implemented |
| M3 | Would-Use scoring | Implemented |
| M3 | Insight validation | Implemented |

---

# 16. Final Project Flow

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

# 17. Next Development Direction

After Milestone 3, possible future work includes stronger evaluation against real-user studies, improved persona segmentation, experiment history, research-report generation and an optional user interface.

These are future extensions and are not required for the current Milestone 3 implementation.
