
from pathlib import Path

FILE_CATEGORIES = {
    "Documents": [".txt", ".pdf", ".doc", ".docx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_category(file_path):
    """Return a category based on the file extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def preview_files(folder_path):
    """Display how files will be organized without moving them."""
    folder = Path(folder_path).expanduser()

    if not folder.exists() or not folder.is_dir():
        print("Error: Please enter a valid folder path.")
        return []

    files = [item for item in folder.iterdir() if item.is_file()]

    if not files:
        print("No files found to organize.")
        return []

    print("\nFile Organization Preview")
    print("-" * 35)

    for file_path in files:
        category = get_category(file_path)
        print(f"{file_path.name} -> {category}/")

    return files


def organize_files(folder_path):
    """Move files into category folders safely."""
    folder = Path(folder_path).expanduser()

    files = preview_files(folder)

    if not files:
        return

    confirmation = input("\nMove these files? (y/n): ").strip().lower()

    if confirmation != "y":
        print("Organization cancelled. No files were moved.")
        return

    moved_count = 0

    for file_path in files:
        category = get_category(file_path)
        destination_folder = folder / category
        destination_file = destination_folder / file_path.name

        if destination_file.exists():
            print(f"Skipped: {file_path.name} (destination already exists)")
            continue

        try:
            destination_folder.mkdir(exist_ok=True)
            file_path.rename(destination_file)
            print(f"Moved: {file_path.name} -> {category}/")
            moved_count += 1
        except OSError as error:
            print(f"Error moving {file_path.name}: {error}")

    print(f"\nOrganization completed. Files moved: {moved_count}")


if __name__ == "__main__":
    selected_folder = input(
        "Enter the folder path to organize: "
    ).strip().strip('"')

    if not selected_folder:
        print("Error: Folder Path cannot be empty.")
    else:
        organize_files(selected_folder)
