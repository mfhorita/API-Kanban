# coding: UTF-8
from http import HTTPStatus  # pragma: no cover

from fastapi import FastAPI  # pragma: no cover
from fastapi.responses import HTMLResponse  # pragma: no cover

app = FastAPI()  # pragma: no cover


@app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root():  # pragma: no cover
    return """
        <html>
          <head>
            <title> Nosso olá mundo!</title>
          </head>
          <body>
            <h1> Olá Mundo </h1>
          </body>
        </html>"""
