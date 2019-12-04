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

SVJ_build_python_path(){
    local Dirs=( "${SVJ_TOP_DIR}"/{,utils} )
    SVJ_build_some_path "$PYTHONPATH" "${Dirs[@]}"
}

# Set environment variables
export SVJ_TOP_DIR="$(SVJ_top_dir)"
export SVJ_EXTERNALS_DIR="${SVJ_TOP_DIR}/external"
export SVJ_MG_FILES_DIR="${SVJ_TOP_DIR}/madgraph"
export SVJ_MODELS_DIR="${SVJ_MG_FILES_DIR}/models"
export SVJ_MG_INPUT_DIR="${SVJ_MG_FILES_DIR}/input_files"
export MG_GENPROD_DIR="${SVJ_TOP_DIR}/external/genproductions/bin/MadGraph5_aMCatNLO"
export PYTHONPATH="$(SVJ_build_python_path)"

CondaVer=3  # make sure this matches the version in conda_init.sh
MINICONDA_DIR=$SVJ_TOP_DIR/external/miniconda${CondaVer}

if [ ! -d $MINICONDA_DIR ]; then
    echo -e "Conda environment has not been set up. Please run \e[1m./conda_init.sh\e[0m, then try again"
    exit
else
    source $MINICONDA_DIR/etc/profile.d/conda.sh
    conda activate svj_env
    export PYTHONNOUSERSITE=true
    export PYTHONPATH="$PWD:$PYTHONPATH"
fi

# Display splash page if terminal is wide enough (otherwise it looks shit)
if (( $COLUMNS >= 159 )); then
    echo -e "\e[1;36m$(cat utils/splash_page.txt)\e[0m"
fi
