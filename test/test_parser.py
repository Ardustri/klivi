from klivi.parser import Parser
from klivi.utils.fs import read_file
from os import path

import unittest


class MyTestCase(unittest.TestCase):
    def test_answer(self):
        parser = Parser(read_file(path.join("mock_data", "sample.html")))
        self.assertIsNone(parser.render())


if __name__ == '__main__':
    unittest.main()
