from pydantic import BaseModel


class MatchedMismatchedWordsRequest(BaseModel):
    sentence1: str
    sentence2: str

class MatchedMismatchedWordsResponse(BaseModel):
    common_words: list
    different_words: list