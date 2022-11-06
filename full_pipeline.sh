#!/bin/bash
# Run pipeline in docker from 0 - 100
docker build -t stackoverflow-sem:1.0 .
docker run --name stackoverflow_artefact -it -v /Users/mikexie/pipeline/stackoverflow_questions.db:/home/stackoverflow_sem/stackoverflow_questions.db stackoverflow-sem:1.0
docker cp stackoverflow_artefact:/home/stackoverflow_sem /Users/mikexie/docker_artefact