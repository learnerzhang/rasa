#!/usr/bin/env bash

# config constants.py

# actions
run actions --action examples.weather.actions

# train nlu
train nlu --config examples/weather/config.yml

# train nlu and core
train --config examples/weather/config.yml --domain examples/weather/domain.yml


# server
run --port 5005 --cors "*" --enable-api -m models/ --endpoints examples/weather/endpoints.yml  --credentials examples/weather/credentials.yml --log-file out.log --debug