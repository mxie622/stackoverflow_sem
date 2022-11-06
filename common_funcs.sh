#!/bin/bash

function mbd_gen {
    python3 /home/stackoverflow_sem/python/run_mbd.py \
    # --pipeline_start_month=${PIPELINE_START_MONTH} \
    # --pipeline_end_month=${PIPELINE_END_MONTH} \
    # --title=${TITLE} \
    # --input_dataset=${INPUT_DATASET} \
    # --output_dataset=${OUTPUT_DATASET}
    "${common_flags[@]}"
}

function feature_gen {
    python3 /home/stackoverflow_sem/python/run_feature.py \
    # --title=$TITLE \
    # --input_dataset=$INPUT_DATASET \
    # --output_dataset=$OUTPUT_DATASET
    "${common_flags[@]}"
}

function sem {
    python3 /home/stackoverflow_sem/python/run_train.py \
    # --title=$TITLE
    "${common_flags[@]}"
}

function pipeline_common_flags {
#    local -n flags=$1
    flags=()
    flags+=(--title=$TITLE)
    flags+=(--pipeline_start_month=$PIPELINE_START_MONTH)
    flags+=(--pipeline_end_month=$PIPELINE_END_MONTH)
}
