
from fastapi import FastAPI
from app.routers import user, matched_mismatched_words, reverse_string, average_words_length
from fastapi import FastAPI,  Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException

app = FastAPI()

app.include_router(user.router)
app.include_router(reverse_string.router)
app.include_router(average_words_length.router)
app.include_router(matched_mismatched_words.router)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )