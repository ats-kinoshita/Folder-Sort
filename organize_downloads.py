
import os
import shutil
from pathlib import Path

# Define the file type categories and their corresponding extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt', '.rtf'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Presentations': ['.ppt', '.pptx'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Programs': ['.exe', '.msi', '.dmg'],
    'Scripts': ['.py', '.sh', '.bat', '.js']
}

def organize_downloads_folder(downloads_folder):
    # Ensure the downloads folder exists
    downloads_path = Path(downloads_folder)
    if not downloads_path.exists():
        print(f"The folder {downloads_folder} does not exist.")
        return

    # Create subfolders for each category
    for category in FILE_CATEGORIES.keys():
        category_folder = downloads_path / category
        category_folder.mkdir(exist_ok=True)

    # Move files to their corresponding category folders
    for item in downloads_path.iterdir():
        if item.is_file():
            file_extension = item.suffix.lower()
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    shutil.move(str(item), str(downloads_path / category / item.name))
                    moved = True
                    break
            if not moved:
                # If the file type is not in the predefined categories, move it to 'Others'
                others_folder = downloads_path / 'Others'
                others_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(others_folder / item.name))

    print("Downloads folder organized successfully.")

# Path to your downloads folder
downloads_folder = 'C:/Users/akino/Downloads'  # Change this to your actual downloads folder path

# Run the script
organize_downloads_folder(downloads_folder)
