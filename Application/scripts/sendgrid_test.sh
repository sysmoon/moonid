#!/bin/bash

curl -i --request POST \
--url https://api.sendgrid.com/v3/mail/send \
--header 'Authorization: Bearer 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' \
--header 'Content-Type: application/json' \
--data '{"personalizations": [{"to": [{"email": "sysmoon@gmail.com"}]}],"from": {"email": "moonkl54@gmail.com"},"subject": "Hello, World!","content": [{"type": "text/plain", "value": "Howdy!"}]}'
