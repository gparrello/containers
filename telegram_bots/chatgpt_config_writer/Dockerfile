FROM ubuntu:latest
WORKDIR /config
RUN echo "{ \"openaisession\": \"$CHATGPT_AUTH_TOKEN\" }" > chatgpt.json

CMD ["tail", "-f", "/dev/null"]