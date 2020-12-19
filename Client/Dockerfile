FROM python:latest
# Put files/file at/in the image '/client/' folder.
RUN mkdir -p /clientdata
COPY client.py /client/
# '/client/' is now the base directory
WORKDIR /client/
# execute the command
CMD [ "python3", "/client/client.py" ]
