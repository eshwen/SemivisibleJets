#!/bin/bash

if [ -z $1 ]; then
    usr_msg="Usage: ./pid_change_t_channel.sh <path to LHE file>"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

lheFile=$1
echo "Changing PIDs for t-channel..."
sed -i 's/49001010/4900101/g' $lheFile
sed -i 's/49001011/4900101/g' $lheFile
sed -i 's/49001012/4900101/g' $lheFile
sed -i 's/49001013/4900101/g' $lheFile
sed -i 's/49001014/4900101/g' $lheFile
echo "Done!"

exit