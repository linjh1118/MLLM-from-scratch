dataset_id=${1:-"wikitext"}
local_dir=${2:-"assets/hf/wikitext"}


export HF_ENDPOINT=https://hf-mirror.com

huggingface-cli download \
  --resume-download \
  $dataset_id \
  --local-dir $local_dir \
  --repo-type dataset

# how to use:
# bash utils/download/hf_cli_model.sh <dataset_repo_id> <where_to_save_dataset>


# you need to do the following to make sure you can use hugingface-cli
# 
# 1. 安装huggingface_hub[cli]
# $pip install -U huggingface_hub[cli]
# 2. 登录。 需先从 https://huggingface.co/settings/tokens 获取 access token
# $huggingface-cli login  # 根据提示输入hf_token即可登录

