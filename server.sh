docker build -t server:1.0 . (command is executed from the directory where dockerfile is stored)
docker volume create servervol
docker network create mynet
docker run --name server -p 9000:9000 --network mynet --mount source=servervol,target=/serverdata server:1.0
