# TravelGuard AI

Agentic Real-Time Application Security Testing

TravelGuard AI is a Python-based security testing project designed to discover APIs, understand business logic, plan tests, validate findings, and report remediation evidence in a controlled travel-booking environment.

## Project goal

This repository is the foundation for a portfolio-ready application security project that helps simulate the workflow of an autonomous DAST-style agent. The system is designed to:

- discover endpoints in a target application,
- classify business workflows,
- generate targeted security tests,
- verify findings with deterministic checks,
- present evidence and remediation guidance,
- support safe retesting after fixes.

## Current status

This repo currently includes the initial project scaffold and a working FastAPI health check endpoint.

## Tech stack

- Python 3
- FastAPI
- Uvicorn
- HTTPX
- Streamlit
- SQLite
- Pydantic
- pytest
- Playwright

## Local setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   # Windows: .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API server:

   ```bash
   uvicorn target_app.main:app --reload
   ```

4. Open the automatic API docs:

   - http://127.0.0.1:8000/docs
   - http://127.0.0.1:8000/redoc

## First endpoint

The application exposes:

- GET /health

Example response:

```json
{
  "status": "ok",
  "service": "travelguard-ai",
  "version": "0.1.0"
}
```

## Repository structure

```text
travelguard-ai/
├── target_app/
│   ├── __init__.py
│   └── main.py
├── agent/
│   └── __init__.py
├── security/
│   └── __init__.py
├── dashboard/
│   ├── __init__.py
│   └── app.py
├── docs/
│   ├── architecture.md
│   └── demo.md
├── tests/
│   └── test_health.py
├── reports/
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Roadmap

Planned milestones:

- build the vulnerable SkyRoute demo app,
- add discovery and endpoint inventory,
- map user roles and business workflows,
- create safe testing and verification logic,
- build a Streamlit dashboard,
- add retesting and evidence reporting.

## Safety note

This project is intended for authorized local testing only. The target environment is a controlled mock travel-booking application used for demonstration and portfolio purposes.
