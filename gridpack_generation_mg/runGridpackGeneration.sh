#!/bin/bash

if [ -z $2 ]; then
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
If the creation fails at any point, rerun with the '-r' option.
The master job will be run locally, and the individual channels will be run on HTCondor.\n\e[0m"

sleep 15

# Initialise proxy of grid cert to home directory so Condor jobs can pick it up
export X509_USER_PROXY=$HOME/x509up_u${UID}
inception=$(( $(date "+%s") - $(date "+%s" -r ${X509_USER_PROXY}) ))
proxy_length_hr=168 # 1 week
proxy_length_s=$(( $proxy_length_hr * 3600 ))
if (( "$inception" < "$proxy_length_s" )); then
    echo "No need to re-initialise proxy as it's still valid"
else
    voms-proxy-init --voms cms --valid ${proxy_length_hr}:00
fi

printf "Submitting. Check on jobs with \e[1mcondor_q $USER\n\e[0m"
./submit_condor_gridpack_generation.sh $model_name $input_cards_dir

# IF RUNNING PRIVATE PRODUCTION, I COULD JUST CUT OUT THE ACTUAL GRIDPACK STAGE AND JUST DOWNLOAD A COPY OF MADGRAPH, PLACE THE MODEL DIRECTORY IN THERE AND RUN. BUT WOULD HAVE TO MAKE SURE MY RUN CARD IS USED AND WOULD NEED TO INCLUDE THE "launch" LINE IN THE PROC CARDS
