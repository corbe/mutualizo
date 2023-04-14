from pydantic import BaseModel


class AverageWordsLengthRequest(BaseModel):
    sentence: str

class AverageWordsLengthResponse(BaseModel):
    sentence: str
    average_lengths: float