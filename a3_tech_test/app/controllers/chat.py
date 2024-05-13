from a3_tech_test.app.modules.models.gemini_api import query_engine
from a3_tech_test.app.interfaces.chat import chat_message
from a3_tech_test.app.utils.logs import CustomLogger

logger = CustomLogger()

async def achat(query: chat_message):
    logger.info(f"Making aquery call")
    
    response = await query_engine.aquery(query.query)
    
    logger.info(f"Response is: {response.response}")  
    
    return {
        "response": response.response # .sources[0].content
    }
