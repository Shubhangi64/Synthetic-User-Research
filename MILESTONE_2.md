# Milestone 2 — Foundation

## Objective
Build the basic foundation of the AI-powered synthetic user research platform.

## Completed components

### 1. Synthetic user research study
The project uses Generative AI to simulate research participants with stable demographic, behavioral and psychological characteristics.

### 2. System architecture
The basic architecture is:

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

### 3. Experiment Workspace
The experiment defines:

- Product
- Product description
- Target audience
- Research objective
- Research questions

Current demonstration product: **AI Personal Shopping Platform**.

### 4. Persona Generation Agent
The agent generates:

- Name
- Age
- Occupation
- Location
- Income
- Personality traits
- Communication style
- Decision-making style
- Shopping behavior
- Price sensitivity
- Brand loyalty
- Review dependence
- Technology adoption
- Goals
- Motivations
- Pain points
- Concerns
- Values
- Product preferences

### 5. Persona Memory and Consistency Foundation
Each interview session keeps an in-memory conversation history. The persona profile is supplied again when generating each answer so the model can preserve identity and behavioral characteristics.

## Milestone 2 demonstration commands

Test API:

```powershell
python main.py --test
```

Generate 20 personas:

```powershell
python main.py --generate-personas 20
```

Display personas:

```powershell
python main.py --show-personas
```

The generated data is stored as JSON. No SQLite database or FastAPI server is required.

## Milestone 2 deliverable

At the end of Milestone 2, the repository contains the experiment definition and a reusable synthetic persona population that becomes the input to Milestone 3.
