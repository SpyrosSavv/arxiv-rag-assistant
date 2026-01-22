from fastapi import APIRouter

router = APIRouter()

@router.get("/ping", tags=["Health"])
async def ping():
    """Simple ping endpoint."""
    return {"status": "ok", "message": "pong"}