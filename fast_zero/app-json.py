# coding: UTF-8
from http import HTTPStatus  # pragma: no cover

from fastapi import FastAPI  # pragma: no cover

from fast_zero.schemas import Message  # pragma: no cover

app = FastAPI()  # pragma: no cover


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():  # pragma: no cover
    return {'message': 'Olá mundo!'}
