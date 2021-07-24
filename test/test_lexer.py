import json
from klivi.lexer import Lexer

import unittest


class MyTestCase(unittest.TestCase):

    def test_answer(self):
        html_content = get_single_line_content('mock_data/sample.html')
        json_content = get_single_line_content('mock_data/sample.json')

        self.assertEqual(
            json.loads(Lexer(html_content).lexify()),
            json.loads(json_content)
        )


def get_single_line_content(path):
    with open(path) as f:
        return f.read().replace('\n', '')


if __name__ == '__main__':
    unittest.main()
