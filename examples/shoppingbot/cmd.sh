#!/usr/bin/env bash

# action
# rasa run actions --action examples.luckin.actions
rasa run actions

# only nlu
rasa train nlu

# only core
rasa train core

# nlu and core
rasa train

# cmd
rasa shell --debug

# server
# rasa run --port 5005 --cors "*" --enable-api -m models/ --endpoints examples/luckin_form/endpoints.yml  --credentials examples/luckin_form/credentials.yml --log-file out.log --debug
rasa run --port 5005 --cors "*" --enable-api -m models/ --endpoints endpoints.yml  --credentials credentials.yml --log-file out.log --debug