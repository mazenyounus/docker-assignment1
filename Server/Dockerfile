FROM python:latest
RUN mkdir -p /serverdata
# Put necessary files in/at the image '/server/' folder.
COPY server.py /server/
COPY send.txt /server/
# '/server/' is now the base directory
WORKDIR /server/
# Expose port 9000 in the container
EXPOSE 9000
# execute the command
CMD [ "python3", "/server/server.py" ]