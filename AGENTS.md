# AGENTS.md

## Commands
- Run all checks with `./scripts/check.sh`. Never invoke `pytest`, `ruff`, or `mypy`
  directly — your shell has no venv active and bare `python3` is 3.9.
- Run the server with `./scripts/dev.sh`. Do not invoke `uvicorn` directly.
- Never run `pip install`. If a dependency is missing, add it to `pyproject.toml` and tell me.

## Layout
- `src/tasker/main.py` — app factory only. No routes beyond `/health`.
- `src/tasker/api/` — one router module per resource. Routing only: no persistence, no business rules.
- `src/tasker/models/` — Pydantic v2 schemas. Separate `XCreate`, `XUpdate`, `XOut` per resource.
- `src/tasker/store/` — persistence, behind a Protocol so the backend can be swapped.
- `tests/` — one file per router, named `test_<resource>.py`.

## Conventions
- Python 3.11+. Everything annotated; `mypy --strict` must pass.
- Pydantic v2 only: `model_validate` / `model_dump`. Never `.dict()` or `.parse_obj()`.
- Every route declares `response_model`. Never return a bare dict from a handler.
- IDs are `uuid.UUID`, generated server-side. Clients never supply an ID on create.
- Timestamps are timezone-aware UTC via `datetime.now(UTC)`.

## Plans
Before any change touching more than two files, write `docs/plans/NNNN-<slug>.md` with:
objective, files to touch, non-goals, how to verify. Update it as you work and commit it
with the change. Read existing plans in `docs/plans/` before proposing new work.

## Code Review Rules

### List endpoints must paginate
Flag any collection endpoint returning an unbounded list.
Safe path: `limit` (default 50, max 200) and `offset` query params, total count in the response.

### No error payloads under a 2xx status
Flag handlers returning an error shape with 200/201.
Safe path: raise `HTTPException` with a 4xx/5xx status.

### Response models must not leak internals
Flag endpoints whose `response_model` is a store or internal dataclass instead of a `*Out` schema.

### No mutable state at module scope
Flag module-level dicts or lists used as storage.
Safe path: build the store in `create_app()` and inject it with a dependency.
Exception: constants and immutable lookup tables.

## Non-goals
- No auth, no database, no Docker, no CI config unless I ask.
- Do not add dependencies.
- Do not reformat files you were not asked to change.
