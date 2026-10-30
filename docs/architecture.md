# TravelGuard AI architecture

## Overview

TravelGuard AI is structured as a layered security testing project:

- Target application: a deliberately vulnerable travel-booking app used for controlled experiments.
- Discovery layer: identifies endpoints, request patterns, and candidate routes.
- Business context layer: maps endpoints to workflows and user roles.
- Agentic planner: selects relevant security tests based on endpoint behavior.
- Verification layer: validates whether a security issue is real.
- Dashboard layer: presents findings, status, and retesting outcomes.

## Planned modules

- `target_app/` — intentionally vulnerable demo application
- `agent/` — endpoint discovery, planning, orchestration
- `security/` — validation logic and deterministic checks
- `dashboard/` — Streamlit frontend
- `reports/` — evidence and remediation outputs

## Current milestone

This repository currently includes the initial FastAPI scaffold and a working /health endpoint.
