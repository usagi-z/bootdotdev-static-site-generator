import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_1(self):
        md = """
# foobar   
# foobaz
"""
        self.assertEqual(extract_title(md), "foobar")
    def test_2(self):
        md = """
foobar
foobaz
"""
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
