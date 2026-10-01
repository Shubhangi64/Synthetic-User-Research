# Generation of AI Powered Synthetic Users for Product Research

An AI-powered synthetic user research platform that generates diverse hypothetical personas and simulates their responses to product research questions using Generative AI.

The system is designed to help researchers perform **early-stage product research, validation, persona analysis, and insight extraction** without requiring a real participant for every exploratory experiment.

> **Current status:** Working Python-based prototype with Gemini, persona generation, fixed-question survey simulation, interview memory, response validation, and insight extraction.
> **Development direction:** The project is being upgraded toward a production-ready architecture using Python, FastAPI, PostgreSQL, ML-based persona analysis, and stateful AI-agent orchestration.

---

## 1. Project Overview

Traditional user research can require significant time, money, and participant availability. This project explores whether Generative AI can create useful **synthetic users** for early-stage product research.

The researcher provides:

* Product description
* Target audience
* Research objective
* Research questions

The system then:

1. Generates synthetic personas.
2. Gives each persona a consistent demographic and behavioral profile.
3. Simulates survey responses.
4. Supports multi-turn persona interviews.
5. Maintains persona and conversation context.
6. Validates response consistency and realism.
7. Extracts research insights.
8. Calculates quantitative response statistics.
9. Identifies recurring themes, concerns, behavioral patterns, and feature preferences.

The generated users are **hypothetical AI-generated participants** and are not replacements for real human participants.

---

# 2. Project Objective

The primary objective is:

> **To develop a Generative AI powered platform for creating synthetic users and simulating product research interactions for early-stage product validation.**

The system focuses on understanding:

* User preferences
* Expectations
* Concerns
* Product feature preferences
* Trust and adoption behavior
* Shopping behavior
* Sentiment
* Agreement and disagreement patterns
* Behavioral trends

---

# 3. Current Demonstration

The current experiment uses an:

### Product

**AI Personal Shopping Platform**

### Target Audience

**Online shoppers aged 18–40**

### Research Objective

> To understand the preferences, expectations, concerns, and behavioral responses of online shoppers toward an AI-powered personal shopping platform.

### Product Features

* AI product recommendations
* Price comparison
* Personalized shopping feed
* Review summarization
* Virtual try-on
* Price-drop alerts
* Budget-based shopping
* Product quality score
* Brand comparison
* Alternative product suggestions
* Return-policy comparison
* AI shopping assistant

---

# 4. System Workflow

```text
Researcher
    |
    v
Experiment Definition
    |
    +-- Product
    +-- Target Audience
    +-- Research Objective
    +-- Research Questions
    |
    v
Persona Generation Agent
    |
    v
Synthetic Personas
    |
    +-- Demographic Attributes
    +-- Personality Traits
    +-- Behavioral Patterns
    +-- Psychological Profile
    +-- Shopping Preferences
    |
    +--------------------+
    |                    |
    v                    v
Survey Mode         Interview Mode
    |                    |
    v                    v
Fixed Questions     Multi-turn Chat
    |                    |
    +---------+----------+
              |
              v
       Response Validation
              |
              v
       Insight Extraction
              |
              +-- Themes
              +-- Sentiment
              +-- Agreement
              +-- Disagreement
              +-- Behavioral Trends
              +-- Feature Preferences
              +-- Would-use Analysis
              |
              v
        Research Results
```

---

# 5. Current Features

## 5.1 Experiment Workspace

The experiment defines the research context:

```text
Product
Target Audience
Research Objective
Research Questions
```

This information is provided to the AI modules as research context.

---

## 5.2 Synthetic Persona Generation

The Persona Generation Agent creates hypothetical users with attributes such as:

* Name
* Age
* Occupation
* Location
* Personality traits
* Behavioral patterns
* Psychological profile
* Price sensitivity
* Brand loyalty
* Review dependence
* Technology adoption

The current experiment contains **20 synthetic personas**.

Example:

```text
Marcus Vance
Age: 34
Occupation: Cybersecurity Analyst
Location: Austin, TX

Personality:
- Analytical
- Skeptical
- Pragmatic
- Privacy-conscious

Behavior:
- Researches products carefully
- Checks multiple reviews
- Compares prices
```

---

# 6. Survey Mode

Survey Mode uses a fixed questionnaire so that every synthetic persona receives the same research questions.

Example questions include:

1. Would you use this AI personal shopping platform? Why or why not?
2. Which feature would be most useful to you?
3. What is your biggest concern about using this platform?
4. Would you trust this platform with your shopping data?
5. How important is price comparison when shopping online?
6. How important are product reviews and review summaries?
7. Would you use virtual try-on?
8. What feature would make you more comfortable using the platform?
9. Would you prefer AI recommendations or make shopping decisions yourself?
10. How likely would you be to use the platform regularly?

Using the same questions enables comparison across personas.

---

# 7. Interview Mode

Interview Mode allows the researcher to select a persona and conduct a multi-turn conversation.

The system provides:

```text
Persona Profile
+
Previous Conversation History
+
Current Question
```

to the LLM.

This allows the persona to maintain consistency across multiple turns.

Example:

```text
Researcher:
Why are you concerned about AI shopping recommendations?

Persona:
I prefer to verify expensive purchases myself because
I do not want an algorithm deciding which products I should buy.
```

A later question can use the previous conversation context.

---

# 8. Persona Memory

The current prototype maintains conversational context using:

```text
Persona Profile
+
Conversation History
```

The long-term production version is planned to use a more structured memory architecture.

Future memory improvements may include:

* Short-term conversation memory
* Long-term persona memory
* Important user opinions
* Previous product interactions
* Semantic memory using embeddings

---

# 9. Response Validation

After generating responses, the validation module evaluates:

* Persona consistency
* Response realism
* Potential issues

Current validation uses an LLM-based evaluator with a 1–5 scoring scale.

Example:

```text
Consistency: 5/5
Realism:     5/5
Status:      PASS
Issues:      None
```

### Important limitation

A high LLM evaluation score does **not** prove that a synthetic persona is equivalent to a real human participant.

Future validation will include:

* Schema validation
* Contradiction detection
* Cross-question consistency checks
* Statistical checks
* Persona similarity analysis
* Human evaluation
* Comparison against real-user research where available

---

# 10. Insight Extraction

The Insight Extraction module analyzes the collected synthetic responses.

It currently extracts:

* Summary
* Recurring themes
* Sentiment
* Agreement patterns
* Disagreement patterns
* Behavioral trends
* Feature preferences
* User concerns
* Segment observations
* Research implications
* Limitations
* Would-use analysis

The system also performs deterministic calculations in Python where appropriate.

For example:

```text
Would-use responses: 20
Average score: 2.4 / 5
```

The distinction between deterministic Python calculations and LLM-generated qualitative analysis helps make the analysis easier to reproduce and inspect.

---

# 11. Current Results

For the current AI Personal Shopping Platform experiment:

```text
Number of synthetic personas: 20

Would-use score distribution:

Score 1 → 5 personas
Score 2 → 6 personas
Score 3 → 5 personas
Score 4 → 4 personas
Score 5 → 0 personas

Average → 2.4 / 5
```

Recurring themes included:

* Data privacy concerns
* Algorithmic bias concerns
* Concerns about sponsored recommendations
* Need for independent verification
* Interest in price comparison
* Interest in review summarization

These results are **synthetic exploratory results** and should not be interpreted as evidence of the actual preferences of the general population.

---

# 12. Technologies Used

## Current Implementation

| Technology       | Purpose                               |
| ---------------- | ------------------------------------- |
| Python           | Main programming language             |
| Gemini           | Generative AI model                   |
| Google GenAI SDK | Gemini API integration                |
| JSON             | Current prototype data storage        |
| Pydantic         | Data validation and structured models |
| python-dotenv    | Environment variable management       |
| Git              | Version control                       |
| GitHub           | Source-code repository                |

---

# 13. Why Python?

Python is used as the primary language because the project is primarily an:

* AI application
* ML/NLP application
* Generative AI system
* Data analysis system

Python provides a strong ecosystem for:

* Machine learning
* NLP
* LLM APIs
* Data processing
* Statistics
* Embeddings
* Clustering
* Backend development

The project will therefore remain **Python-centric**, even as additional technologies are introduced.

---

# 14. Why Gemini?

The current prototype uses a Gemini Flash-family model through Google's GenAI SDK.

The model was selected for the prototype based on:

* Fast response generation
* Suitability for high-volume synthetic responses
* Structured output capabilities
* Python SDK support
* Availability and cost considerations

The project does not assume that one LLM is permanently the best choice.

A future AI-provider abstraction will allow different models to be evaluated without changing the main research system.

---

# 15. Current Project Architecture

The current implementation is a modular Python application.

```text
main.py
   |
   +---- config.py
   |
   +---- ai_client.py
   |
   +---- experiment.py
   |
   +---- personas.py
   |
   +---- survey.py
   |
   +---- interview.py
   |
   +---- validation.py
   |
   +---- insights.py
```

### `main.py`

Acts as the main controller/CLI entry point.

### `config.py`

Contains experiment configuration and research settings.

### `ai_client.py`

Centralizes communication with the Gemini API.

### `experiment.py`

Handles experiment and JSON data loading/saving.

### `personas.py`

Responsible for synthetic persona generation.

### `survey.py`

Runs the fixed-question survey.

### `interview.py`

Provides interactive multi-turn persona interviews.

### `validation.py`

Evaluates persona response consistency and realism.

### `insights.py`

Extracts and summarizes research insights.

---

# 16. Current Data Storage

The prototype currently uses JSON files.

```text
data/
├── experiment.json
├── personas.json
├── personas_generated.json
├── survey_results.json
└── validation_results.json
```

This approach was selected for the initial prototype because it is:

* Simple
* Easy to inspect
* Easy to debug
* Suitable for a small research experiment
* Easy to version as research artifacts

However, JSON files are not the intended long-term storage architecture for a multi-user production application.

---

# 17. Planned Production Database

The production version will use **PostgreSQL**.

A planned schema includes:

```text
users
experiments
personas
questions
responses
interviews
messages
validations
insights
reports
```

Example relationship:

```text
User
 |
 +-- Experiments
       |
       +-- Personas
       |
       +-- Questions
       |
       +-- Responses
       |
       +-- Interviews
       |
       +-- Insights
       |
       +-- Reports
```

PostgreSQL is suitable because the application contains many relationships between research entities.

---

# 18. Planned Backend Architecture

The production architecture is planned as:

```text
                Streamlit / Web UI
                       |
                       v
                    FastAPI
                       |
                       v
                Service Layer
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
 Persona Service  Survey Service  Interview Service
        |              |              |
        +--------------+--------------+
                       |
                       v
                 AI / ML Layer
                       |
              +--------+--------+
              |                 |
              v                 v
           Gemini          ML Models
              |                 |
              +--------+--------+
                       |
                       v
                  PostgreSQL
```

---

