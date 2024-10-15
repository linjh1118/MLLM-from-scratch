import os

def rename_files(log_file):
    with open(log_file, 'r') as log:
        for line in log:
            parts = line.strip().split()
            if len(parts) >= 9:
                moved_from = parts[1]
                moved_to = parts[3]
                symlink_target_name = os.path.basename(moved_to)

                # 获取移动后的文件名
                wrong_mv_name = os.path.join(os.path.dirname(moved_to), moved_from.split('/')[-1])
                moved_file_name = os.path.join(os.path.dirname(moved_to), symlink_target_name)
                
                print(f'ready to rename {wrong_mv_name} to {moved_file_name}')
                
                # 如果目标文件存在并且不是一个符号链接，则重命名
                if os.path.exists(wrong_mv_name) and not os.path.islink(wrong_mv_name):
                    try:
                        os.rename(wrong_mv_name, moved_file_name)
                        print(f"Renamed {wrong_mv_name} to {moved_file_name}")
                    except Exception as e:
                        print(f"Failed to rename {wrong_mv_name} to {moved_file_name}: {e}")
                else:
                    print(f"{wrong_mv_name} does not exist or is already a symlink.")

if __name__ == "__main__":
    log_file = "log_mv"
    rename_files(log_file)

# first ==> bash mv.sh 2>&1 | tee log_mv
# second ==> python rename.py
