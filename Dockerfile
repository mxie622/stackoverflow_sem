FROM sem-stackoverflow-base:1.0

USER root
ENV ROOT_DIR .
ENV SRC_DIR ${ROOT_DIR}/app
ENV BASH_DIR ${ROOT_DIR}/bash

RUN mkdir -p /home/stackoverflow_sem

COPY . /home/stackoverflow_sem

ENV TITLE="stackoverflow"
ENV PIPELINE_START_MONTH="202201" 
ENV PIPELINE_END_MONTH="202205" 
ENV FEATURE_MAPPING="stackoverflow_sem_feature_mapping.csv" 
ENV INPUT_DATASET=${BASH_DIR}
ENV OUTPUT_DATASET=${BASH_DIR}

RUN pip install -r ${ROOT_DIR}/requirements.txt

RUN chmod a+x ${ROOT_DIR}/*.sh || true

ENTRYPOINT ${ROOT_DIR}/run_pipeline.sh