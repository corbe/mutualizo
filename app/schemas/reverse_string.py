from pydantic import BaseModel

class ReverseStringRequest(BaseModel):
    number: int

class ReverseStringResponse(BaseModel):
    number: int
    reverted_number: int