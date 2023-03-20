# Spider Web

Bem vindo ao spider_web, projeto que tem como objetivo unir documentação e código.

### Setup

***O processo de setup do projeto ainda está em desenvolvimento, mas há algumas informações cruciais que serão repassadas na lista abaixo:***

#### Backend:
Pasta `spider_web`

- É preciso habilitar a extensão unnacent do postgresql, por conta da pesquisa full text que é implementada em algumas partes desse projeto. Para isso, acesse o seu banco de dados e rode ```CREATE EXTENSION unaccent;```.

- O projeto usa django rest framework no backend.

- O projeto usa poetry como gerenciador de bibliotecas.

- Para rodar o processo django já com o banco de dados, vá ao terminal e rode ```docker compose up``` na pasta spider_web.

- O lint do projeto na parte do backend fica por conta de `black` e `isort`. Portanto, um ```black .;isort .``` no terminal formatará o código para você.

- Ao rodar `docker compose up`, o processo do django rodará na porta 8999.

#### Frontend:
Pasta `front-spider-web`

- O frontend do projeto está usando **vuejs 3** e **tailwind css**. O tailwind foi escolhido por tornar o desenvolvimento css prático, mas ter um peso pequeno.

- Para rodar o lint, é só executar `npm run format` (formatar) ou `npm run lint` (lint).

- O real objetivo do projeto é criar um bom backend, ao ponto de o front ser uma casquinha facilmente trocável.

- Para rodar o backend na porta 3999, basta executar `npm run dev`.
