FROM node:14-buster-slim as build

WORKDIR /app
COPY package.json ./
RUN npm install
RUN npm i @sveltejs/kit@1.0.0-next.123
COPY . .
RUN npm run build

FROM node:14-buster-slim as public
WORKDIR app
COPY --from=build /app .
EXPOSE 3000
CMD ["node", "./build"]
