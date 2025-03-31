FROM python:3.12
ENV POETRY_VIRTUALENVS_CREATE=false
ENV DATABASE_URL=${{ secrets.DATABASE_URL }}
ENV SECRET_KEY=${{ secrets.SECRET_KEY }}
ENV ALGORITHM=${{ secrets.ALGORITHM }}
ENV ACCESS_TOKEN_EXPIRE_MINUTES=${{ secrets.ACCESS_TOKEN_EXPIRE_MINUTES }}

WORKDIR app/
COPY . .

RUN pip install poetry
RUN pip install uvicorn
RUN pip install email_validator
RUN pip install "python-multipart"

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 fast_zero.app:app
