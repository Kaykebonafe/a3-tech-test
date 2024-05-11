from a3_tech_test.app.modules.models.gemini_api import get_query_engine
from a3_tech_test.app.interfaces.chat import chat_message


async def achat(query: chat_message):
    query_engine = await get_query_engine()
    
    response = await query_engine.achat(query.query)  
    
    return response
