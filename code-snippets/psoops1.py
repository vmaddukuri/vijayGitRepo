import math
import os
import sys
from pprint import PrettyPrinter


class Demo:
    pass


d = Demo()
print(d)
print(Demo)
print(__name__)  # namespace of a script, module
print(math.__name__)
print(os.__name__)
print(sys.__name__)
print(PrettyPrinter)