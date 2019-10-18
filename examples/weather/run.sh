#!/usr/bin/env bash

# train
rasa train --data data --out models -c config.yml

# actions server
rasa run actions

# web server
rasa run -m models --enable-api --port 5002 --endpoints endpoints.yml  --credentials credentials.yml --log-file out.log
