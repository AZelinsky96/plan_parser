#!/bin/bash

FROM python:3.8

RUN mkdir /plan_parser

COPY / /plan_parser
COPY pyproject.toml /plan_parser

WORKDIR /plan_parser
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

ENTRYPOINT [ "python3" ]

CMD [ "plan_parser/app.py" ]
