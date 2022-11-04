FROM node:16-alpine3.15

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@4.5.13 -g

COPY frontend/package.json .
COPY frontend/package-lock.json .
RUN npm install

CMD ["npm", "run", "serve"]
