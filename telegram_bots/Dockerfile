FROM ghcr.io/m1guelpf/chatgpt-telegram
WORKDIR /root
RUN echo "{ \"openaisession\": \"$CHATGPT_AUTH_TOKEN\" }" > config.json

ENTRYPOINT ["/bin/chatgpt-telegram"]