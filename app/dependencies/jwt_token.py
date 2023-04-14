
from fastapi_jwt_auth import AuthJWT
from ..schemas.settings import Settings


from fastapi import  Depends

@AuthJWT.load_config
def get_config():
    return Settings()


async def verify_token(Authorize: AuthJWT = Depends()):  
    Authorize.jwt_required()