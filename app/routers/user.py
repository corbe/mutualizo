from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from ..schemas.jwt_token import JWTToken
from ..schemas.user import User
from ..services.user import UserService

router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)


@router.post('/')
def login(user: User, authorize: AuthJWT = Depends()):

    """
    Realiza o login e retorna o access_token para chamada dos endpoints

    :param user: User {"username": str, "password":str}
    
    :return { access_token: str }:
    """

    username = user.username
    password = user.password

    userService = UserService(authorize)
    access_token = userService.login(username, password)

     # Cria o objeto de resposta
    login_response = JWTToken(
            access_token=access_token
    )

    return login_response