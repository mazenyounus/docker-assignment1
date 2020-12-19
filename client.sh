docker build -t client:1.0 . (command is executed from the directory where dockerfile is stored)
docker volume create clientvol
docker run --name client --network mynet --mount source=clientvol,target=/clientdata client:1.0
