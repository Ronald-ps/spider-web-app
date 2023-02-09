FROM python:3.11-slim

WORKDIR /app

# já copio tudo de uma vez só porque a aplicação é pequena
COPY . .

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
RUN pip install poetry==1.3.1
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install -n --no-ansi --no-root

# expondo a porta do django
EXPOSE 8000

# execuções quando o container inicia
CMD ["./docker/commands/pre_start.sh"]
