#!/bin/bash

if [ -z $1 ]; then
    echo "------------------------------------------------
Usage: ./tChannelPIDChange.sh <path to LHE file>
------------------------------------------------"
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