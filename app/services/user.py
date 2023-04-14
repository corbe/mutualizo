from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi import HTTPException

class UserService:

    """
    Realiza o login

    :param username: str
    :param password: str
    
    :return { access_token: str }:
    """
    
    def __init__(self, authorize: AuthJWT):
        self.authorize = authorize

    def login(self, username: str, password:str):

        if username != "test" or password != "test":
            raise HTTPException(status_code=401,detail="Bad username or password")


        # subject identifier for who this token is for example id or username from database
        access_token =  self.authorize.create_access_token(subject=username)
        return access_token