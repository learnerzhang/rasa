#!/usr/bin/env bash
# only nlu
rasa train nlu

# train
# rasa train --config examples/luckin/config.yml --domain examples/luckin/domain.yml --data examples/luckin/data
rasa train --data data --out models -c config.yml

# actions server
rasa run actions


# cmd shell
rasa shell

# web server
# rasa run --port 5005 --cors "*" --enable-api -m models/ --endpoints endpoints.yml  --credentials credentials.yml --log-file out.log --debug
rasa run -m models --cors "*"  --enable-api --port 5005 --endpoints endpoints.yml  --credentials credentials.yml --log-file out.log
rasa run -m models --endpoints endpoints.yml
