# 📦 Importing essentials
from fastapi import FastAPI
from routers import telemetry
from dotenv import load_dotenv

# 🐍 Importing services
from services.health import check_health

# 🌐 Load environment variables
load_dotenv()

# 🚀 Initializing the FastAPI app
app = FastAPI(
    title="MetryFlow Backend",  # Application Title
    description="Centralized backend of MetryFlow",  # Application Description
    version="1.0.0",  # Version of the API
)

# 🛠️ Include telemetry and metrics routers
app.include_router(telemetry.router, prefix="/telemetry", tags=["Telemetry"])
app.include_router(telemetry.router, prefix="/metrics", tags=["Metrics"])

# 💚 Health Check Endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint that uses the check_health service to verify
    the status of the application and MongoDB.
    """
    return await check_health()