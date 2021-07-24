from klivi.parser import Parser
from klivi.utils.fs import read_file


def test_answer():
    parser = Parser(read_file("sample.html"))
    assert parser.render() == None
