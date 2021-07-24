import json
from klivi.lexer import Lexer

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_answer(self):
        html_content = ""
        json_content = ""

        with open("mock_data/sample.html", "r") as html_file:
            html_content = html_file.read().replace("\n", "")
            html_file.close()

        with open("mock_data/sample.json", "r") as json_file:
            json_content = json_file.read().replace("\n", "")
            json_file.close()

        self.assertEqual(
            json.loads(Lexer(html_content).lexify()),
            json.loads(json_content)
        )


if __name__ == '__main__':
    unittest.main()
