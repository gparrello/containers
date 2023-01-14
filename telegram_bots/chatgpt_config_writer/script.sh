#!/bin/bash

echo "{ 'openaisession': '$CHATGPT_AUTH_TOKEN' }" > /config/chatgpt.json
tail -f /dev/null


