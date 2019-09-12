from decimal import Decimal
from decimal import InvalidOperation
from ant.validata import driver

parser = [driver.Letter('-'), driver.Letter('+')]


class Parser(object):
    def __init__(self):
        pass

    def validata(self, letter):
        return True



def validata(s):
    for l in s:
        parser.validata(l)


def validata(s):
    try:
        Decimal(s)
        return True
    except InvalidOperation:
        return False


def main():
    print validate('e.0')



