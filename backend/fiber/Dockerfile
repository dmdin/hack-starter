FROM golang
WORKDIR /go/src/app
EXPOSE 80

RUN go get github.com/githubnemo/CompileDaemon

CMD ["CompileDaemon", "-command=./app"]