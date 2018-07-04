# Functions to make and extend environment variables
SVJ_top_dir(){
  local Canonicalize="readlink -f"
  $Canonicalize asdf &> /dev/null || Canonicalize=realpath
  dirname "$($Canonicalize "${BASH_SOURCE[0]}")"
}

SVJ_build_some_path(){
    local NewPath="$1" ;shift
    for dir in "$@";do
	if ! $( echo "$NewPath" | grep -q '\(.*:\|^\)'"$dir"'\(:.*\|$\)' ); then
	    NewPath="${dir}${NewPath:+:${NewPath}}"
	fi
    done
    echo "$NewPath"
}

SVJ_build_sys_path(){
    local Dirs=( "${SVJ_EXTERNALS_DIR}"/pip/bin )
    Dirs+=( {"$SVJ_cvmfs_PythonDir","$SVJ_cvmfs_PipDir"}/bin)
    SVJ_build_some_path "$PATH" "${Dirs[@]}"
}

SVJ_build_python_path(){
    local Dirs=( "${SVJ_TOP_DIR}"/{,Utils} "${SVJ_EXTERNALS_DIR}"/pip/lib/python2.7/site-packages )
    Dirs+=( {"$SVJ_cvmfs_PythonDir","$SVJ_cvmfs_PipDir"}/lib/python2.7/site-packages/ )
    SVJ_build_some_path "$PYTHONPATH" "${Dirs[@]}"
}

# Source Python, pip, gcc and ROOT from cvmfs
SVJ_cvmfs_PythonDir=/cvmfs/sft.cern.ch/lcg/releases/Python/2.7.13-597a5/x86_64-slc6-gcc62-opt/
SVJ_cvmfs_PipDir=/cvmfs/sft.cern.ch/lcg/releases/pip/8.1.2-c9f5a/x86_64-slc6-gcc62-opt/
SVJ_cvmfs_GCCSetup=/cvmfs/sft.cern.ch/lcg/contrib/gcc/6.2/x86_64-slc6/setup.sh
SVJ_cvmfs_RootSetup=/cvmfs/sft.cern.ch/lcg/releases/LCG_88/ROOT/6.08.06/x86_64-slc6-gcc62-opt/bin/thisroot.sh
source "${SVJ_cvmfs_GCCSetup}"
source "${SVJ_cvmfs_RootSetup}"

# Set environment variables
export SVJ_TOP_DIR="$(SVJ_top_dir)"
export SVJ_EXTERNALS_DIR="$(SVJ_top_dir)/external"
export SVJ_MODELS_DIR="$(SVJ_top_dir)/MG_models"
export SVJ_MG_INPUT_DIR="$(SVJ_top_dir)/MG_input_files"
export MG_GENPROD_DIR="${SVJ_TOP_DIR}/external/genproductions/bin/MadGraph5_aMCatNLO"
export PYTHONPATH="$(SVJ_build_python_path)"
export PATH="$(SVJ_build_sys_path)"

# Install required Python packages
python -m pip install --prefix "${SVJ_EXTERNALS_DIR}"/pip -U setuptools --ignore-installed
python -m pip install --prefix "${SVJ_EXTERNALS_DIR}"/pip -r requirements.txt --ignore-installed

unset SVJ_cvmfs_{PythonDir,PipDir,GCCSetup,RootSetup}

# Display splash page if terminal is wide enough (otherwise it looks shit)
if (( $COLUMNS >= 159 )); then
    echo -e "\e[1;36m$(cat Utils/splash_page.txt)\e[0m"
fi