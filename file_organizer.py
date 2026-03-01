import os
import shutil

# Configuration
path = "./test_folder"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".JPG", ".PNG"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}

# 1. Validate path exists
if not os.path.exists(path):
    print(f"Error: Path '{path}' does not exist!")
    exit()

# Create folders
for folder in file_types:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 2. Get files only (exclude directories)
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# Move files
for file in files:
    file_path = os.path.join(path, file)
    moved = False
    
    for folder, extensions in file_types.items():
        if any(file.lower().endswith(ext.lower()) for ext in extensions):
            dest_path = os.path.join(path, folder, file)
            
            # 3. Handle existing files
            if os.path.exists(dest_path):
                name, ext = os.path.splitext(file)
                dest_path = os.path.join(path, folder, f"{name}_copy{ext}")
            
            shutil.move(file_path, dest_path)
            moved = True
            break
    
    if not moved:
        dest_path = os.path.join(path, "Others", file)
        if os.path.exists(dest_path):
            name, ext = os.path.splitext(file)
            dest_path = os.path.join(path, "Others", f"{name}_copy{ext}")
        shutil.move(file_path, dest_path)

print("✅ Files organized successfully!")
