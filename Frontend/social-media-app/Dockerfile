FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app/Frontend

COPY package*.json ./

RUN npm install

COPY . . /app/Frontend/

EXPOSE 8080

CMD [ "http-server", "dist" ]