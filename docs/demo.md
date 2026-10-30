# TravelGuard AI demo notes

This repository is being built as a beginner-friendly cybersecurity project.

## Initial milestone

The repository now includes:

- a FastAPI application,
- a working `/health` endpoint,
- a minimal dashboard placeholder,
- a health test,
- a project structure for the future agent architecture.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn target_app.main:app --reload
```

Then open:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
