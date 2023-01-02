# SPDX-FileCopyrightText: 2021, 2022 ImpulsoGov <contato@impulsogov.org>
# SPDX-License-Identifier: MIT

FROM python:3.10.6

# Configurar variáveis de ambiente
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV POETRY_VIRTUALENVS_CREATE 1
ENV POETRY_VIRTUALENVS_IN_PROJECT 0
ENV IMPULSOGAETL_AMBIENTE "producao"
ENV GAETL_LOG_NIVEL=INFO 

# atualizar repositórios
RUN apt-get clean all -qq
RUN apt-get update -yqq
RUN apt-get dist-upgrade -yqq
RUN apt-get autoremove -yqq
RUN python3 -m pip install --upgrade pip

# Criar e logar em novo usuário; copiar configurações e atribuir permissões
RUN useradd --create-home appuser
WORKDIR /home/appuser
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN chown -R appuser /home/appuser
USER appuser

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/home/appuser/.local/bin:$PATH"

# Instalar dependências Python
RUN poetry install --no-dev --no-root

# copiar código-fonte e instalar pacote impulsoetl
COPY README.md ./README.md
COPY src ./src
RUN poetry install --no-dev

# Executar o ponto de entrada contendo os scripts
CMD [ "poetry", "run", "impulso-google-analytics"]