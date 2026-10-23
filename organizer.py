from pathlib import Path

# Folder containing our sample files
TEST_FOLDER = Path("test_files")

# File extensions and their categories
FILE_CATEGORIES = {
    "Documents": [".txt", ".pdf", ".doc", ".docx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".7z"],
}

def get_category(file_path):
    """Find the category of a file using its extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def preview_files():
    """Preview file categories without moving files."""
    if not TEST_FOLDER.exists():
        print(f"Error: Folder not found: {TEST_FOLDER}")
        return

    files = [
        item for item in TEST_FOLDER.iterdir()
        if item.is_file()
    ]

    if not files:
        print("No files found to organize.")
        return

    print("\nFile Organization Preview")
    print("-" * 35)

    for file_path in files:
        category = get_category(file_path)
        print(f"{file_path.name} -> {category}/")


def organize_files():
    """Move files into folders based on their extensions."""
    if not TEST_FOLDER.exists():
        print(f"Error: Folder not found: {TEST_FOLDER}")
        return

    files = [
        item for item in TEST_FOLDER.iterdir()
        if item.is_file()
    ]

    if not files:
        print("No files found to organize.")
        return

    for file_path in files:
        category = get_category(file_path)
        destination_folder = TEST_FOLDER / category

        # Create the destination folder if needed
        destination_folder.mkdir(exist_ok=True)

        destination_file = destination_folder / file_path.name

        # Avoid overwriting a file with the same name
        if destination_file.exists():
            print(f"Skipped: {file_path.name} (already exists)")
            continue

        file_path.rename(destination_file)
        print(f"Moved: {file_path.name} -> {category}/")

    print("\nFile organization completed!")


if __name__ == "__main__":
    preview_files()
    print("\nStarting Organization")
    organize_files()