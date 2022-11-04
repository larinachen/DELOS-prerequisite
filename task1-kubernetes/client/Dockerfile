# Get the latest base image for python
FROM python:latest
# Put files at the image '/server/' folder.
ADD client.py /client/
# '/server/' is base directory
WORKDIR /client/
# Expose listening port in the container
ENV PORT "$LISTEN_PORT"
EXPOSE ${PORT}
# execute the command
CMD [ "python3", "/client/client.py" ]