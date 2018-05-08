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

# Unset some env variables as gcc setup in my setup script causes errors when compiling MadGraph source directory
unset LD_LIBRARY_PATH
unset FC
unset COMPILER_PATH
unset PYTHONPATH
unset CC
unset COMPILER_PATH
unset CXX

./submit_gridpack_generation.sh 3000 3000 1nd $model_name $input_cards_dir 1nh

echo "Check on the job status with \`bjobs\`"

#./gridpack_generation.sh $model_name $input_cards_dir 1nd

exit

# IF RUNNING PRIVATE PRODUCTION, I COULD JUST CUT OUT THE ACTUAL GRIDPACK STAGE AND JUST DOWNLOAD A COPY OF MADGRAPH, PLACE THE MODEL DIRECTORY IN THERE AND RUN. BUT WOULD HAVE TO MAKE SURE MY RUN CARD IS USED AND WOULD NEED TO INCLUDE THE "launch" LINE IN THE PROC CARDS