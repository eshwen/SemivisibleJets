#!/bin/bash

if [ -z $1 ]; then
    echo "------------------------------------------------
Usage: ./tChannelPIDChange.sh <path to LHE file>
------------------------------------------------"
fi

lheFile=$1

echo "Changing PIDs for s-channel..."

sed -i 's/5000521/4900101/g' $lheFile

echo "Done!"

exit