#!/bin/bash

if [ -z $1 ]; then
    echo "---------------------------------------------------------------------
Usage ./runGridpackGeneration.sh model_name rel_path(input_cards_dir)
---------------------------------------------------------------------"
    exit
fi

: "${SVJ_TOP_DIR:?Certain environment variables do not exist. Please source the setup script first.}; exit"

model_name=$1
input_cards_dir=$2

cd $MG_GENPROD_DIR

./gridpack_generation.sh $model_name $input_cards_dir 1nd

exit
