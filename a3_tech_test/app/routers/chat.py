from fastapi import APIRouter
from a3_tech_test.app.interfaces.chat import chat_message
from a3_tech_test.app.controllers.chat import achat
from a3_tech_test.app.utils.logs import CustomLogger

logger = CustomLogger()

router = APIRouter()

logger.info("Route initialized")

@router.post(
    path="/query"
)
async def chat_completion(
    query: chat_message
):
    logger.info("Route called")
    
    data = await achat(query=query)
    
    logger.info("Request successfully done, returning response.")
    
    return data