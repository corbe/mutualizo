

from fastapi import APIRouter, Depends
from ..dependencies.jwt_token import verify_token
from ..schemas.matched_mismatched_words import MatchedMismatchedWordsRequest, MatchedMismatchedWordsResponse
from ..services.matched_mismatched_words import MatchedMismatchedWords

router = APIRouter(
    prefix="/matched-mismatched-words",
    tags=["matched-mismatched-words"],
    dependencies=[Depends(verify_token)],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def matched_mismatched_words(matchedMismatchedWords: MatchedMismatchedWordsRequest):
    
    # Atribui parametro do payload as variáveis de sentença
    sentence1 = matchedMismatchedWords.sentence1
    sentence2 = matchedMismatchedWords.sentence2

    matchedMismatchedWords = MatchedMismatchedWords()
    common_words,different_words = matchedMismatchedWords.matched_mismatched_words(sentence1, sentence2)

    # Cria e monta o objeto de resposta MatchedMismatchedWordsResponse
    averageWordsLengthResponse= MatchedMismatchedWordsResponse(
        common_words=common_words,
        different_words=different_words
        )

    # Retorna uma tupla com as duas listas
    return averageWordsLengthResponse
