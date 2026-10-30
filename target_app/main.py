from fastapi import FastAPI

app = FastAPI(
    title="TravelGuard AI",
    description="Agentic security testing API for a travel-booking test environment.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "travelguard-ai",
        "version": "0.1.0",
    }
