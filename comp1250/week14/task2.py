# 101475343
# philip bezalel asher ranillo

import os
import sys

def count_files_and_dirs(path):
    if not os.path.exists(path):
        raise FileNotFoundError("The path not found")
    total_count = 0
    files_count = 0
    folders_count = 0
    for root, dirs, files in os.walk(path):
        folders_count += len(dirs)
        files_count += len(files)

    folders_count += 1

    total_count = folders_count + files_count
    return total_count, folders_count, files_count

try:
    path = input("Enter a path: ")
    total_count, folders_count, files_count = count_files_and_dirs(path)
    print(f"The number of files and directories is", total_count)
    print(f"The number of files", files_count)
    print(f"The number of folders", folders_count)
except FileNotFoundError as Err:
    print("Error: ", Err, file=sys.stderr)