from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create the tasker application."""
    application = FastAPI(title="tasker", version="0.1.0")

    @application.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return application


app = create_app()
