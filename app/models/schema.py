from pydantic import BaseModel

class LogicRequest(BaseModel):
    text: str

class LogicResponse(BaseModel):
    input: str
    analysis: str
    status: str