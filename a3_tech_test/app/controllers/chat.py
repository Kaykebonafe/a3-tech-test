from a3_tech_test.app.modules.models.gemini_api import query_engine
from a3_tech_test.app.interfaces.chat import chat_message

async def achat(query: chat_message):
    response = await query_engine.aquery(query.query)  
    
    return {
        "response": response.response # .sources[0].content
    }
