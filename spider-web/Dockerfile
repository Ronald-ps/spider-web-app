FROM python:3.11.0

WORKDIR /app

# copio o pyproject para instalação de dependências
COPY pyproject.toml poetry.lock ./

# Evita de usar o sistema legado e instala dependências necessárias
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		python-dev \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*
  # evita de armazenar arquivos referencia de pacotes que não serão usadas pra nada,
  # já que a imagem já foi criada

# instalação de dependencias python
RUN python3 -m pip install --upgrade pip
RUN pip install poetry==1.3.2
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install -n --no-ansi --no-interaction --no-cache --verbose --no-root

# Resto do projeto, menos o que está em dockerignore
COPY . .

# expondo a porta do django
EXPOSE 8000

# execuções quando o container inicia. Ele procura a pasta dentro do host, nao dentro do container
CMD ["./.docker/commands/pre_start.sh"]
