#!/bin/bash

if [ -z $1 ]; then
    usr_msg="Usage: ./pid_change.sh <path to LHE file>"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

lheFile=$1
echo "Changing PDGIDs from MadGraph to Pythia conventions in preparation for hadronisation..."
# madgraph sign convention is reversed?
# Change PDGIDs for dark quarks
sed -i 's/-5000521/-4900101/g' $lheFile
sed -i 's/-49001010/4900101/g' $lheFile
sed -i 's/-49001011/4900101/g' $lheFile
sed -i 's/-49001012/4900101/g' $lheFile
sed -i 's/-49001013/4900101/g' $lheFile
sed -i 's/-49001014/4900101/g' $lheFile

sed -i 's/5000521/4900101/g' $lheFile
sed -i 's/49001010/-4900101/g' $lheFile
sed -i 's/49001011/-4900101/g' $lheFile
sed -i 's/49001012/-4900101/g' $lheFile
sed -i 's/49001013/-4900101/g' $lheFile
sed -i 's/49001014/-4900101/g' $lheFile

# Change PDGIDs for t-channel bi-fundamentals
sed -i 's/9000005/4900001/g' $lheFile
sed -i 's/9000006/4900001/g' $lheFile
sed -i 's/9000007/4900001/g' $lheFile
sed -i 's/9000008/4900001/g' $lheFile
sed -i 's/9000009/4900003/g' $lheFile
sed -i 's/9000010/4900003/g' $lheFile
sed -i 's/9000011/4900003/g' $lheFile
sed -i 's/9000012/4900003/g' $lheFile
sed -i 's/9000013/4900005/g' $lheFile
sed -i 's/9000014/4900005/g' $lheFile
sed -i 's/9000015/4900005/g' $lheFile
sed -i 's/9000016/4900005/g' $lheFile
sed -i 's/9000017/4900002/g' $lheFile
sed -i 's/9000018/4900002/g' $lheFile
sed -i 's/9000019/4900002/g' $lheFile
sed -i 's/9000020/4900002/g' $lheFile
sed -i 's/9000021/4900004/g' $lheFile
sed -i 's/9000022/4900004/g' $lheFile
sed -i 's/9000023/4900004/g' $lheFile
sed -i 's/9000024/4900004/g' $lheFile
sed -i 's/9000025/4900006/g' $lheFile
sed -i 's/9000026/4900006/g' $lheFile
sed -i 's/9000027/4900006/g' $lheFile
sed -i 's/9000028/4900006/g' $lheFile
echo "Done!"

exit
