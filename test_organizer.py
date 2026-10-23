
import unittest
from pathlib import Path
from organizer import get_category


class TestFileOrganizer(unittest.TestCase):

    def test_text_file(self):
        self.assertEqual(
            get_category(Path("notes.txt")), "Documents"
        )

    def test_pdf_file(self):
        self.assertEqual(
            get_category(Path("report.pdf")), "Documents"
        )

    def test_image_file(self):
        self.assertEqual(
            get_category(Path("photo.jpg")), "Images"
        )

    def test_archive_file(self):
        self.assertEqual(
            get_category(Path("backup.zip")), "Archives"
        )

    def test_unknown_file(self):
        self.assertEqual(
            get_category(Path("data.xyz")), "Others"
        )


if __name__ == "__main__":
    unittest.main()
