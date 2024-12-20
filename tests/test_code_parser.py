import unittest
from modules.code_parser import parse_code

class TestCodeParser(unittest.TestCase):
    def test_parse_code(self):
        parsed_data = parse_code("data/sample_code.py")
        self.assertTrue("classes" in parsed_data)
        self.assertTrue("functions" in parsed_data)

if __name__ == "__main__":
    unittest.main()
