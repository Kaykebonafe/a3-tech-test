from fastapi import APIRouter, Request, Response
from a3_tech_test.app.interfaces.chat import chat_message
from a3_tech_test.app.controllers.chat import achat


router = APIRouter()

@router.post(
    path="/completion"
)
async def chat_completion(
    request: Request,
    response: Response,
    query: chat_message
):
    data = await achat(query=query)
    
    return data