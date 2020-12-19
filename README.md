# docker-assignment1

I have created the client and server programs using sockets.

Server Container:

Run 'fileserver.sh' in the server root folder using command: 'sh server.sh'.

This script will create the network as 'mynet' with a random and anonymous subnet.

It will create the volume for server as 'servervol'.

In the Server Dockerfile, I have used a base image 'python:latest' and then installed the necesarry packages/apks.

It will also automatically build the image named as 'server:1.0'(as that is the name I am giving it) using the Dockerfile placed in the folder named as 'server' which will a send  file of size 20 bytes in '/serverdata' directory(which is attached to 'servervol' volume in the container) to the client container.

The server sends file to the client or establishes communications by using sockets.

Now, I am running the server container named as 'server'.


Client Container:

Coming to 'fileclient.sh', run this script in the client root folder using command: 'sh client.sh'.

It will create the volume for client named as 'clientvol'.

It will also automatically build the image named as 'clientimage:1.0' using Dockerfile placed in the folder named as 'client'.

I have used the same base image as used for server 'python:latest' in the Dockerfile and installed the necessary packages/apks.

The client will download/get the file from the server using 'sockets'(I couldn't do the verification of checksum).

The '/clientdata' directory is attached to the volume named as 'clientvol', so that the received file will get saved in the 'clientvol' volume as well

To run the client container named as 'client' in the shell mode instead of just running the application by default, we'll have too use -it in the docker run command after run or we can also enter the container shell using docker exec -it client bash/sh

Once inside the client container, one go to the '/clientdata directory' and fire 'ls' command to check the files in the directory.




The server sends file to the client or they establishes communication with each other by using sockets but that is not enough as I am containerizing them and I want the containers to communicate.

The socket needs host and port number to connect and/or bind. In the host, we'll have to specify the IP address and in port, a port number. So, we'll specify the IP address of the server container and a random port number(in this case 9000, which is also the port being exposed in the server Dockerfile). In this way the client will know to get connected to the server container with the IP address specified to the client container.

And also, the client container and server container should be in a user-defined network(in this case mynet).
