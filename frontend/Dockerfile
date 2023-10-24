FROM node:14-alpine as build

WORKDIR app
COPY package.json ./
RUN npm i
RUN npm i @sveltejs/kit@1.0.0-next.123
COPY . .
RUN npm run build

FROM node:14-alpine as prepare
WORKDIR app
COPY --from=build /app/build ./build
COPY --from=build /app/package.json .
RUN npm i --only=prod


FROM alpine as public
WORKDIR app
RUN apk add --update nodejs
COPY --from=prepare /app .

EXPOSE 3000
CMD ["node", "./build"]
