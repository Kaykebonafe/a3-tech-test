from fastapi import APIRouter

router = APIRouter()

@router.get(path="/")
async def root():
    return "A3 Tech Test is alive!"