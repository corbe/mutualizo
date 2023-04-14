# in production you can use Settings management
# from pydantic to get secret key from .env
from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = "encYlMDjpB6GTpTAVzkzvWBze4GnmjEm"