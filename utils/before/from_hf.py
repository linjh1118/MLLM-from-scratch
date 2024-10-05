# contribute by [MrChen-NEU](https://github.com/MrChen-NEU)! Thanks for contribution!

from huggingface_hub import snapshot_download
import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--repo_id', type=str, default="THUDM/cogvlm2-llama3-chinese-chat-19B")
parser.add_argument('--local_dir', type=str, default='assets/hf/THUDM/cogvlm2-llama3-chinese-chat-19B')
args = parser.parse_args()

# 设置代理
# os.environ["http_proxy"] = "http://localhost:7890"
# os.environ["https_proxy"] = "http://localhost:7890"

# 
""" 1. huggingface_hub指南
需要登陆的模型：
huggingface_hub.login("HF_TOKEN") # token 从 https://huggingface.co/settings/tokens 获取
"""

""" 2. 参数说明
allow_patterns选择需要下载的文件类型,通过ignore_patterns设置需要忽略的文件类型。
resume_download=True,表示允许断点续传, 整个很有必要。
etag_timeout=100,超时阈值,默认10秒,这里自己根据情况修改。
"""

i = 0
while True:
    try:
        snapshot_download(
            local_dir=local_dir,
            repo_id=repo_id,
            repo_type="model",  # "dataset" or "model"
            local_dir_use_symlinks=False,
            resume_download=True,
            ignore_patterns=["*.msgpack",
                             "*.h5",
                             "*.ot"]
            )
    except Exception as e :
        print(f'{repo_id} download failed at {i} times, error: {e}, will retry...\n' * 5)
    else:
        print(f'{repo_id} download success!\n' * 10)
        break
    

