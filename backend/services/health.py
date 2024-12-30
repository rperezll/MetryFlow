# 📦 Importing essentials
from fastapi import HTTPException

# 📦 Importing mongodb modules
from db import db
from pymongo.errors import ServerSelectionTimeoutError

async def check_health():
    """
    Checks the health of the application and the MongoDB service.
    Returns a status dictionary if everything is ok, raises HTTPException if not.
    """
    try:
        # Intenta hacer un ping al servidor MongoDB
        ping_response = await db.command('ping')
        return {"status": "ok", "database": "MongoDB is up and running"}
    except ServerSelectionTimeoutError as e:
        raise HTTPException(status_code=503, detail=f"MongoDB is not available")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
