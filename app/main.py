from fastapi import FastAPI

from app.routes import health
from app.routes import version
from app.routes import services

app = FastAPI(
    title="DevSecure Pipeline",
    description="DevSecOps application and deployment platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "DevSecure Pipeline is running!"
    }


app.include_router(health.router)
app.include_router(version.router)
app.include_router(services.router)