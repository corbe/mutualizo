

from ..dependencies.jwt_token import verify_token
from fastapi import APIRouter, Depends
from ..schemas.reverse_string import ReverseStringRequest, ReverseStringResponse
from ..services.reverse_string import ReverseStringService

router = APIRouter(
    prefix="/reverse-string",
    tags=["reverse-string"],
    dependencies=[Depends(verify_token)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", dependencies=[Depends(verify_token)])
async def reverse_string(reverseString: ReverseStringRequest):   
    
    """
    Dado um número inteiro, como parâmetro, devolver o
    número inteiro com dígitos invertidos.

    :param number: int
    
    :return { reverted_number: int }:
    """
    
    # Atribui parametro do payload a variável number
    number = reverseString.number

    # Chama o service que reverte a string
    reverseStringService = ReverseStringService()
    number, reverted_number = reverseStringService.reverse_string(number) 
    
    # Cria o objeto de resposta
    reverse_string_response = ReverseStringResponse(
            number=number, 
            reverted_number=reverted_number
    )

    return reverse_string_response