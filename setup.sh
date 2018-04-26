SVJ_top_dir(){
  local Canonicalize="readlink -f"
  $Canonicalize asdf &> /dev/null || Canonicalize=realpath
  dirname "$($Canonicalize "${BASH_SOURCE[0]}")"
}

export SVJ_TOP_DIR="$(SVJ_top_dir)"
export MG_GENPROD_DIR="${SVJ_TOP_DIR}/genproductions/bin/MadGraph5_aMCatNLO"

# Install required Python packages
pip install -r requirements.txt --user --ignore-installed