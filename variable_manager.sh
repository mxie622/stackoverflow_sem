#!/bin/bash

DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
pushd ${DIR}
# Build image for train or predict
export FEATURE_MAPPING=${FEATURE_MAPPING}
export PIPELINE_START_MONTH=${PIPELINE_START_MONTH}
export PIPELINE_END_MONTH=${PIPELINE_END_MONTH}
export INPUT_DATASET=${INPUT_DATASET}
export OUTPUT_DATASET=${OUTPUT_DATASET}
export TITLE=${TITLE}
popd