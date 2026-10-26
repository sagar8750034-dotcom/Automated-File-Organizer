
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from organizer import get_category, preview_files, organize_files


class TestFileOrganizer(unittest.TestCase):

    def test_text_file(self):
        self.assertEqual(get_category(Path("notes.txt")), "Documents")

    def test_pdf_file(self):
        self.assertEqual(get_category(Path("report.pdf")), "Documents")

    def test_image_file(self):
        self.assertEqual(get_category(Path("photo.jpg")), "Images")

    def test_archive_file(self):
        self.assertEqual(get_category(Path("backup.zip")), "Archives")

    def test_unknown_file(self):
        self.assertEqual(get_category(Path("data.xyz")), "Others")

    def test_invalid_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing_folder = Path(temp_dir) / "missing"
            with patch("builtins.print") as mock_print:
                result = preview_files(missing_folder)

            self.assertEqual(result, [])
            mock_print.assert_called()

    def test_empty_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch("builtins.print") as mock_print:
                result = preview_files(temp_dir)

            self.assertEqual(result, [])
            mock_print.assert_called()

    def test_preview_finds_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "notes.txt"
            file_path.write_text("sample", encoding="utf-8")

            result = preview_files(temp_dir)

            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].name, "notes.txt")

    def test_cancel_does_not_move_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "notes.txt"
            file_path.write_text("sample", encoding="utf-8")

            with patch("builtins.input", return_value="n"):
                with patch("builtins.print"):
                    organize_files(temp_dir)

            self.assertTrue(file_path.exists())


if __name__ == "__main__":
    unittest.main()
