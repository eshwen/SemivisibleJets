#!/bin/bash

if [ -z $1 ]; then
    usr_msg="Usage ./runGridpackGeneration.sh model_name rel_path(input_cards_dir)"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
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

printf "\e[1;33mSometimes gridpack generation can fail.
MadGraph is quite temperamental and so can fail when running subprocess for a model.
When running on batch, disk quotas can also be exceeded.
If the creation fails at any point, simply remove the directory created in $MG_GENPROD_DIR and retry.\n\e[0m"

sleep 15

# For running on the grid, but get monitoring as if it's interactive
#./gridpack_generation.sh $model_name $input_cards_dir 1nd

# For running on the grid with CMSConnect
n_cores=1
mem_req="4 Gb"

# Initialise proxy of grid cert to /afs/ so Condor jobs can pick it up
export X509_USER_PROXY=/afs/cern.ch/user/${USER:0:1}/$USER/x509up_u${UID}
inception=$(( $(date "+%s") - $(date "+%s" -r ${X509_USER_PROXY}) ))
proxy_length_hr=168 # 1 week
proxy_length_s=$(( $proxy_length_hr * 3600 ))
if (( "$inception" < "$proxy_length_s" )); then
    echo "No need to re-initialise proxy as it's still valid"
else
    voms-proxy-init --voms cms --valid ${proxy_length_hr}:00
fi

echo nohup ./submit_cmsconnect_gridpack_generation.sh $model_name $input_cards_dir $n_cores "$mem_req" > ${model_name}.debug 2>&1 &
echo "Job submitted. Check on it with \"condor_q $USER\""
# ^^^ FIX THE JOB SUBMISSION

#exit

# IF RUNNING PRIVATE PRODUCTION, I COULD JUST CUT OUT THE ACTUAL GRIDPACK STAGE AND JUST DOWNLOAD A COPY OF MADGRAPH, PLACE THE MODEL DIRECTORY IN THERE AND RUN. BUT WOULD HAVE TO MAKE SURE MY RUN CARD IS USED AND WOULD NEED TO INCLUDE THE "launch" LINE IN THE PROC CARDS
