#!/bin/env python
class Male:
    """ Concrete Class """

    def __init__(self, name):
        self.name = name
        print("Hello Mr." + self.name)


class Female:
    """ Concrete Class """

    def __init__(self, name):
        self.name = name
        print("Hello Miss." + self.name)


class Factory(object):
    """ Factory Class """

    def getPerson(self, name, gender):
        """ Factory Method """
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    """ Invoking the Factory pattern """
    factory = Factory()
    factory.getPerson("chetan", "M")
