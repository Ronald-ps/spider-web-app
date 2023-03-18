# Spider Web

Bem vindo ao spider_web, projeto que tem como objetivo servir para unir documentação e código.

### Setup

***O processo de setup do projeto ainda está em desenvolvimento, mas há algumas informações cruciais que serão repassadas na lista abaixo:***

- É preciso habilitar a extensão unnacent do postgresql, por conta da pesquisa full text que é implementada em algumas partes desse projeto. Para isso, acesse o seu banco de dados e rode ```CREATE EXTENSION unaccent;```

- O projeto usa django rest framework no backend.

- O projeto usa poetry como gerenciador de bibliotecas.

- Para rodar o processo django já com o banco de dados, vá ao terminal e rode ```docker compose up```.
