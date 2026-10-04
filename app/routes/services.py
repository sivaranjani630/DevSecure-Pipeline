from fastapi import APIRouter
from app.models import Service

router = APIRouter()


@router.get("/services")
def get_services():
    services = [
        Service(name="api", status="running"),
        Service(name="database", status="running"),
        Service(name="cache", status="running")
    ]

    return {
        "services": services
    }