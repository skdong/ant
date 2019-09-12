import abc


class Driver(object):
    def __init__(self):
        self.over = False

    @abc.abstractmethod
    def validata(self, letter):
        pass

    def close(self):
        self.over = True


class Letter(Driver):
    def __init__(self, letter):
        super(Letter, self).__init__()
        self.letter = letter

    def validata(self, letter):
        if letter != self.letter:
            return False


class Letters(Driver):
    def __init__(self, letters):
        super(Letters, self).__init__()
        self.letters = letters

    def validata(self, letter):
        if letter not in self.letters:
            return False


class NumDriver(Driver):
    def validata(self, letter):
        return self.parser(letter)

    def __init__(self, parser):
        super(NumDriver, self).__init__()
        self.parser = parser


class ZeroOrOne(NumDriver):
    def validata(self, letter):
        return self.parser(letter)


class ZeroOrMany(NumDriver):
    def validata(self, letter):
        return self.parser(letter)


class OneOrMany(NumDriver):
    def validata(self, letter):
        return self.parser(letter)