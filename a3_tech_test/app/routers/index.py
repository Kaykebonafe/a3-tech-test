from fastapi import APIRouter, Request, Response

router = APIRouter()

@router.get(path="/")
async def root():
    return "A3 Tech Test is alive!"