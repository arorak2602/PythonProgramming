# PythonFileOrganizer

import os
import shutil

print("Welcome to the file organizer")

folderPath = input("Enter the path to folder to organize:\n")

# File type categories
fileTypes = {
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Documents": ["pdf", "txt", "docx", "doc"],
    "Music": ["mp3", "wav"],
    "Videos": ["mp4", "mkv", "avi"],
    "Archives": ["zip", "rar", "7z"]
}

# Loop through all files in the folder
for file in os.listdir(folderPath):
    filePath = os.path.join(folderPath, file)

    # Skip directories
    if os.path.isdir(filePath):
        continue

    ext = file.split(".")[-1].lower()
    moved = False

    # Check file type and move accordingly
    for folder, extensions in fileTypes.items():
        if ext in extensions:
            targetFolder = os.path.join(folderPath, folder)

            if not os.path.exists(targetFolder):
                os.mkdir(targetFolder)

            shutil.move(filePath, os.path.join(targetFolder, file))
            print(f"Moved {file} -> {folder}")
            moved = True
            break

    # Move uncategorized files
    if not moved:
        otherFolder = os.path.join(folderPath, "Others")

        if not os.path.exists(otherFolder):
            os.mkdir(otherFolder)

        shutil.move(filePath, os.path.join(otherFolder, file))
        print(f"Moved {file} -> Others")

print("Organization Completed!")