#!/bin/env python

""" Delegator """
class RealPrinter:
    """ The Delegate """

    def printOut(self):
        print "Printing : something"

class Printer:
    """ The Delegator """
    def __init__(self):
        self.p = RealPrinter()

    def printOut(self):
	self.p.printOut()

if __name__ == '__main__':
    p = Printer()
    p.printOut()

