#!/bin/bash
echo "----test----"
set -e
set -u
set -x

DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
# DIR="$( ls ./pipeline/ && cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
echo "$DIR"
pushd ${DIR}
#echo "--------"
source common_funcs.sh 
source variable_manager.sh

pipeline_common_flags common_flags

mbd_gen
feature_gen
sem