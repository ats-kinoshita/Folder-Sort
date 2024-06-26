# Folder Sort

Python scripts to automatically organize folders by moving files into subfolders based on their file types. 

# organize_downloads.py
Helps keep your downloads folder neat and makes it easier to find files.

## Features

- Organizes files into predefined categories such as Images, Documents, Spreadsheets, Presentations, Archives, Audio, Videos, Programs, and Scripts.
- Moves files with unknown extensions into an "Others" folder.
- Creates category folders if they do not already exist.
- Can be run multiple times without creating duplicate folders.

## File Categories

The script organizes files into the following categories based on their extensions:

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Documents:** `.pdf`, `.doc`, `.docx`, `.txt`, `.odt`, `.rtf`
- **Spreadsheets:** `.xls`, `.xlsx`, `.csv`
- **Presentations:** `.ppt`, `.pptx`
- **Archives:** `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
- **Audio:** `.mp3`, `.wav`, `.aac`, `.flac`
- **Videos:** `.mp4`, `.avi`, `.mkv`, `.mov`
- **Programs:** `.exe`, `.msi`, `.dmg`
- **Scripts:** `.py`, `.sh`, `.bat`, `.js`
- **Others:** Any file types not listed above

## Installation

1. Clone the repository:

    \`\`\`bash
    git clone https://github.com/ats-kinoshita/Folder-Sort.git
    \`\`\`

2. Navigate to the project directory:

    \`\`\`bash
    cd folder-sort
    \`\`\`

3. (Optional) Create a virtual environment and activate it:

    \`\`\`bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use \`venv\Scripts\activate\`
    \`\`\`

4. Install any necessary dependencies (none required for this script).

## Usage

1. Open the script file \`organize_downloads.py\`.

2. Change the path to your downloads folder in the script:

    \`\`\`python
    downloads_folder = 'C:/Users/{YourUsername}/Downloads'  # Change this to your actual downloads folder path
    \`\`\`

3. Run the script:

    \`\`\`bash
    python organize_downloads.py
    \`\`\`

4. The script will organize your downloads folder by moving files into appropriate subfolders.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
