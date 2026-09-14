# src/tasker/api — router rules

- Routers stay thin: validate input, delegate to the store, shape the response.
- Each module exposes `router: APIRouter` with an explicit `prefix` and `tags`.
- Register routers in `create_app()` only. Never call `include_router` from inside this package.
- Obtain the store via `Depends(get_store)`. Never import a store singleton.
- Path params are typed `UUID`. Missing resource raises `HTTPException(404, "task not found")`.
