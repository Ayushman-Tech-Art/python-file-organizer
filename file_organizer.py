import os
import shutil

# Set directory path (change this to your test folder path)
path = "./test_folder"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}

# Create folders if not exist
for folder in file_types:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files into folders
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if any(file.endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(path, folder, file))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(path, "Others", file))

print("Files organized successfully!")
