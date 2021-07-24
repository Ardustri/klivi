from klivi.parser import Parser
from klivi.utils.fs import read_file
from os import path


def test_answer():
    parser = Parser(read_file(path.join("mock_data", "sample.html")))
    assert parser.render() == None
