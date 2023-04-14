from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from ..routers import user, matched_mismatched_words, reverse_string, average_words_length

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 


def start_application():
    app = FastAPI()
    app.include_router(user.router)
    app.include_router(reverse_string.router)
    app.include_router(average_words_length.router)
    app.include_router(matched_mismatched_words.router)

    return app

@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a  app on each test case.
    """
    _app = start_application()
    yield _app


@pytest.fixture(scope="function")
def client(
    app: FastAPI
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClientand
    dependency that is injected into routes.
    """
    with TestClient(app) as client:
        yield client