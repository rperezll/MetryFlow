# 📦 Importing types modules
from pydantic import BaseModel
from typing import Dict

class TelemetryEvent(BaseModel):
    """
    ✨ Telemetry Event Model:
    - **installation_id**: Unique identifier for the installation.
    - **timestamp**: The time when the event occurred.
    - **framework**: Framework used in the application (e.g., FastAPI, Django).
    - **framework_version**: Version of the framework.
    - **platform**: The platform where the app is running (e.g., localhost, Docker).
    - **platform_details**: Detailed information about the platform (optional).
    """
    installation_id: str
    timestamp: str
    framework: str
    framework_version: str
    platform: str
    platform_details: Dict[str, str]
