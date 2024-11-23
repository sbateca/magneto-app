FROM public.ecr.aws/lambda/python:3.11

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --only main --no-dev
COPY ./app app/

CMD ["app.main.aws_lambda_handler"]
