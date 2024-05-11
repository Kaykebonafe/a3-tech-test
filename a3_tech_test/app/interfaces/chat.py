from pydantic import BaseModel, Field

class chat_message(BaseModel):
    query: str = Field(
        ...,
        description="Entrada do usuário."
    )
