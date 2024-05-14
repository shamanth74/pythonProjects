import os
import shutil

def copy_files(source_dir, target_dir, file_extension, visited_dirs):
    count = 0
    for root, dirs, files in os.walk(source_dir):
        if root not in visited_dirs:
            for file in files:
                if file.endswith(f".{file_extension}"):
                    source_file = os.path.join(root, file)
                    target_file = os.path.join(target_dir, file)
                    if not os.path.exists(target_file):
                        try:
                            shutil.copy2(source_file, target_dir)
                            count += 1
                        except Exception as e:
                            print(f"Error copying file {source_file}: {e}")
            visited_dirs.add(root)
    return count

type = str(input("Enter type of file -->"))
source_dir = "D:/"
target_dir = f"D:/{type}_files"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

visited_dirs = set()
count = copy_files(source_dir, target_dir, type, visited_dirs)
print(f"Total {count} files of type {type} copied to {target_dir}")
