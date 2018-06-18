#!/bin/bash
# Script to print usage of bash scripts. Requires setup.sh to be sourced

usr_msg="$1"
line_length=${#usr_msg}
wrap_str=`printf '%0.s-' $(seq 1 $line_length)`
echo "$wrap_str
$usr_msg
$wrap_str"
exit