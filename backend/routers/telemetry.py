# 📦 Importing router essentials
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models.telemetry import TelemetryEvent

# 📦 Importing mongodb modules
from db import metrics_collection
from pymongo import ASCENDING

# 🌐 Initialize the router for telemetry endpoints
router = APIRouter()

# 🛠️ Endpoint for receiving telemetry events
@router.post("/events")
async def receive_event(event: TelemetryEvent):
    """
    🎯 Receives telemetry event data and stores it in the database.
    - **installation_id**: The unique identifier of the installation.
    - **timestamp**: The timestamp of when the event occurred.
    - **framework**: The framework used (e.g., FastAPI, Django).
    - **framework_version**: The version of the framework.
    - **platform**: The platform where the application is running (e.g., Localhost, Docker).
    """
    try:
        result = await metrics_collection.insert_one(event.dict())
        return {"message": "Event received and stored successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 🛠️ Endpoint to retrieve stored metrics
@router.get("/metrics", response_model=List[TelemetryEvent])
async def get_metrics(
    installation_id: Optional[str] = None,
    framework: Optional[str] = None,
    platform: Optional[str] = None,
    limit: int = 10,
    skip: int = 0
):
    """
    🎯 Retrieves stored telemetry metrics based on filter parameters.
    - **installation_id**: Filter by installation ID (optional).
    - **framework**: Filter by framework name (optional).
    - **platform**: Filter by platform (optional).
    - **limit**: Limit the number of results (default is 10).
    - **skip**: Skip the first N results (default is 0).
    """
    query = {}

    # 🧩 Build the query based on the filters
    if installation_id:
        query["installation_id"] = installation_id
    if framework:
        query["framework"] = framework
    if platform:
        query["platform"] = platform

    metrics = []
    async for event in metrics_collection.find(query).skip(skip).limit(limit).sort("timestamp", ASCENDING):
        metrics.append(TelemetryEvent(**event))

    return metrics
