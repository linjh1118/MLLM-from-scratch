#!/bin/bash

# 检查当前目录及其子目录中的符号链接，并将指向的实际文件移动到符号链接所在的位置
find . -type l | while read -r link; do
    # 获取符号链接的目标路径
    target=$(readlink -f "$link")
    # 获取符号链接的名称
    symlink_name=$(basename "$link")
    # 获取符号链接的父目录
    symlink_dir=$(dirname "$link")

    # 如果目标文件与符号链接不在同一目录，则移动文件，并删除原有符号链接
    if [ "$(dirname "$target")" != "$symlink_dir" ]; then
        # 移动文件到符号链接所在位置
        mv "$target" "$symlink_dir"
        # 删除旧的符号链接
        rm "$link"
        echo "Moved $target to $symlink_dir/$symlink_name and removed the old symlink."
    else
        echo "Symbolic link $link points to a file in the same directory. No action needed."
    fi
done

# push this file to datasets/MMMU/MMMU/.
# it will mv the file linked by symblink to symblink
# bash mv.sh 2>&1 | tee log_mv
