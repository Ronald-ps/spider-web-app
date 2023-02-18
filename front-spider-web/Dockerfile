FROM node:14.19.3

WORKDIR /front

# copio o package.json para poder instalar as dependências do proejto
COPY package-lock.json package.json ./

# instala as dependencias
RUN npm install

# Resto do projeto, menos o que está em dockerignore
COPY . .

# expondo a porta do django
EXPOSE 3000
