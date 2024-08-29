import os
import shutil
import datetime

source_dir = "/path/to/source_directory"
backup_dir = "/path/to/backup_directory"

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_folder = os.path.join(backup_dir, f"backup_{current_time}")
os.makedirs(backup_folder)

def backup_files(source, destination):
    if os.path.exists(source):
        for item in os.listdir(source):
            s = os.path.join(source, item)
            d = os.path.join(destination, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        print(f"Backup completed successfully to {destination}")
    else:
        print(f"Source directory {source} does not exist")

backup_files(source_dir, backup_folder)
