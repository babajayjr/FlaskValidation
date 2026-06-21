# ARCHITECT-generated Dockerfile — generic
FROM ubuntu:22.04

WORKDIR /app
COPY . .

EXPOSE 8080

CMD ["sh", "-c", "echo 'No start command'"]
