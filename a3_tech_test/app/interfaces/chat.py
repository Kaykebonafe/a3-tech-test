from pydantic import BaseModel, Field

class chat_message(BaseModel):
    query: str = Field(
        default=None,
        description="Entrada do usuário."
    )