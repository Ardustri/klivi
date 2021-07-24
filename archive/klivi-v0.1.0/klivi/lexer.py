import json
import xmltodict


class Lexer:
    """
    klivi lexer
    """

    def __init__(self, source) -> None:
        self.source = source

    def lexify(self):
        return json.dumps(xmltodict.parse(self.source), indent=4)
