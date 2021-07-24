import json
from klivi.lexer import Lexer


def test_answer():
    html_content = ""
    json_content = ""

    with open("sample.html", "r") as html_file:
        html_content = html_file.read().replace("\n", "")
        html_file.close()

    with open("sample.json", "r") as json_file:
        json_content = json_file.read().replace("\n", "")
        json_file.close()

    assert json.loads(Lexer(html_content).lexify()) == json.loads(json_content)
