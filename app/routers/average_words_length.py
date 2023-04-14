

from fastapi import APIRouter
from fastapi import Depends
from ..dependencies.jwt_token import verify_token
from ..schemas.average_words_length import AverageWordsLengthRequest, AverageWordsLengthResponse
from ..services.average_words_length import AverageWordsLengthService


router = APIRouter(
    prefix="/average-words-length",
    tags=["average-words-length"],
    dependencies=[Depends(verify_token)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", dependencies=[Depends(verify_token)])
def average_words_length(averageWordsLength: AverageWordsLengthRequest):
    """
    Para uma determinada frase, receber uma frase como parâmetro e devolver o
    comprimento médio das palavras..

    :param sentence: str

    :return { average_lengths: float, sentence: str }
    """

    # Atribui parametro do payload a variável number
    sentence = averageWordsLength.sentence

    # Chama o service que reverte a string
    average_words_length_service = AverageWordsLengthService()
    sentence, average_lengths = average_words_length_service.average_words_length(sentence)

    # Cria e monta o objeto de resposta AverageWordsLengthResponse
    averageWordsLengthResponse= AverageWordsLengthResponse(
        sentence=sentence,
        average_lengths=average_lengths
        )

    # Retorna o comprimento médio das palavras.
    return averageWordsLengthResponse