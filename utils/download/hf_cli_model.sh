model_id=${1:-"THUDM/cogvlm2-llama3-chinese-chat-19B"}
local_dir=${2:-"assets/hf/THUDM/cogvlm2-llama3-chinese-chat-19B"}


export HF_ENDPOINT=https://hf-mirror.com

huggingface-cli download \
  --resume-download \
  $model_id \
  --local-dir $local_dir \
  --exclude "*.msgpack" "*.onnx" "*.ot" "*.h5"
  # --exclude "*\.(msgpack\|h5\|ot)"

# how to use:
# bash utils/download/hf_cli_model.sh <model_repo_id> <where_to_save_model>


# you need to do the following to make sure you can use hugingface-cli
# 
# 1. 安装huggingface_hub[cli]
# $pip install -U huggingface_hub[cli]
# 2. 登录【PS: 从 https://huggingface.co/settings/tokens 获取access token】
# $huggingface-cli login  # PS: 之后根据提示输入hf_token



# 上边不是最优选项了
# 将以上东西写到bashrc中，或者终端会话中直接执行
# ⭐️
# export HF_ENDPOINT=https://hf-mirror.com
# export HF_HOME=/workspace/common/ljh/hf_home/
# huggingface-cli --resume-download download Qwen/Qwen2-VL-2B-Instruct
# /workspace/common/ljh/hf_home/hub/models--Qwen--Qwen2-VL-2B-Instruct/snapshots/aca78372505e6cb469c4fa6a35c60265b00ff5a4

