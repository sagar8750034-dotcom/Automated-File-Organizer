# Automated File Organizer

A Python-based utility that organizes files into category-specific folders based on their file extensions. It allows users to select a folder, preview the organization plan, and confirm before moving files.

## Features

- Automatically categorizes files by extension.
- Supports Documents, Images, Videos, Archives, and Others.
- Allows users to specify the folder they want to organize.
- Previews file categories before moving files.
- Asks for user confirmation before organizing files.
- Creates destination folders automatically.
- Prevents overwriting files with duplicate names.
- Handles invalid folder paths and file-moving errors.
- Includes automated unit tests using Python's `unittest` framework.

## Technologies Used

- Python
- pathlib
- unittest
- tempfile
- unittest.mock

## Project Structure

```text
Automated-File-Organizer/
├── organizer.py
├── test_organizer.py
├── README.md
├── .gitignore
└── test_files/
    ├── Documents/
    ├── Images/
    ├── Archives/
    └── Videos/
```

## Supported File Categories

| Category | Extensions |
|---|---|
| Documents | `.txt`, `.pdf`, `.doc`, `.docx` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Videos | `.mp4`, `.mkv`, `.mov` |
| Archives | `.zip`, `.rar`, `.7z` |
| Others | Other unsupported extensions |

## Requirements

- Python 3.10 or later recommended.
- No external Python packages are required.

## How to Run

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Run the program:

```bash
python organizer.py
```

4. Enter the full path of the folder you want to organize when prompted.
5. Review the preview and enter `y` to move files or `n` to cancel.

**Important:** The program moves files from the selected folder. Test it with sample files first and back up important files before organizing them.

## Run Tests

Run the following command to execute the automated unit tests:

```bash
python -m unittest test_organizer -v
```

The test suite checks file categorization, invalid and empty folders, file preview, and cancellation behavior.

## Future Improvements

- Add automatic renaming for duplicate filenames.
- Add logging and a summary report.
- Add a graphical user interface.
- Expand test coverage for file-moving errors and confirmation scenarios.

## Author

Sagar Singh

## License

This project is available for educational and learning purposes.