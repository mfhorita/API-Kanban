# coding: UTF-8
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, todo, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todo.router)


@app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
# Primeira página de boas vindas
def read_root():
    return """
    <html>
      <head>
        <title>Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
