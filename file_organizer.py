import os
import shutil

directory_to_organize = 'path_to_your_directory'

file_types = {
    "Documents": ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    "Music": ['.mp3', '.wav', '.aac', '.flac'],
    "Archives": ['.zip', '.rar', '.tar', '.gz', '.bz2'],
    "Scripts": ['.py', '.js', '.sh', '.bat'],
    "Others": []  
}

def create_folder():
    for folder in file_types.keys():
        folder_path = os.path.join(directory_to_organize, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files():
    for item in os.listdir(directory_to_organize):
        item_path = os.path.join(directory_to_organize, item)

        if os.path.isfile(item_path):
            file_moved = False
            for folder, extensions in file_types.items():
                if any(item.lower().endswith(ext) for ext in extensions):
                    shutil.move(item_path, os.paht.join(directory_to_organize,folder, item))
                    file_moved = True
                    break
                if not file_moved:
                    shutil.move(item_path, os.paht.join(directory_to_organize,"Others". item))
        
def organize_file():
    create_folder()
    move_files()
    print("File have been orgainzed.")


organize_file()