FROM ghcr.io/m1guelpf/chatgpt-telegram
WORKDIR /root/.config
RUN echo "{ \"openaisession\": \"$CHATGPT_AUTH_TOKEN\" }" > chatgpt.json

ENTRYPOINT ["/bin/chatgpt-telegram"]