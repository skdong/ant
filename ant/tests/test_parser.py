import unittest
from ant.validata import parser

class ParserTest(unittest.TestCase):
    def test_validate(self):
        assert parser.validate('1') == False


