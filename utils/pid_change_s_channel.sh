#!/bin/bash

if [ -z $1 ]; then
    usr_msg="Usage: ./pid_change_s_channel.sh <path to LHE file>"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

lheFile=$1
echo "Changing PIDs for s-channel..."
sed -i 's/5000521/4900101/g' $lheFile
echo "Done!"
exit