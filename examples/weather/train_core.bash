#!/usr/bin/env bash

# train core
python -m rasa_core.train -s stories.md -d domain.yml -o models/dialogue --epochs 500 --nlu_threshold 0.4  --core_threshold 0.4


python ./render.py

python -m rasa_core.run -d models/dialogue -u default/current \
       --port 5002 --credentials credentials.yml \
       --cors * --endpoints endpoints.yml