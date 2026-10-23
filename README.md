# Automated File Organizer

A Python-based utility that automatically organizes files into category-specific folders based on their file extensions.

## Features

- Automatically categorizes files by extension.
- Supports Documents, Images, Videos, Archives, and Others.
- Creates destination folders automatically.
- Moves files into their respective category folders.
- Prevents overwriting files with duplicate names.
- Provides a preview before organizing files.
- Includes automated unit tests using Python's `unittest` framework.

## Technologies Used

- Python
- pathlib
- unittest

## Project Structure

```text
Automated-File-Organizer/
├── organizer.py
├── test_organizer.py
├── README.md
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
3. Place the files you want to organize inside `test_files/`.
4. Run the program:

```bash
python organizer.py
```

The program displays a preview and then moves files into their respective category folders.

**Important:** Test the program on sample files first. It moves files from the source folder, so do not use important personal files without a backup.

## Run Tests

Run the following command to execute the automated unit tests:

```bash
python -m unittest test_organizer -v
```

The tests verify file categorization for text files, PDF files, images, archives, and unknown extensions.

## Future Improvements

- Add a command-line interface for selecting folders.
- Add logging and improved error handling.
- Support duplicate filenames with automatic renaming.
- Add an option to preview changes without moving files.

## Author

Sagar Singh

## License

This project is available for educational and learning purposes.
