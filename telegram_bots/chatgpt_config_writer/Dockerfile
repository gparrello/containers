FROM ubuntu:latest
WORKDIR /config
RUN echo "{ \"openaisession\": \"$CHATGPT_AUTH_TOKEN\" }" > chatgpt.json

ENTRYPOINT ["tail", "-f", "/dev/null"]