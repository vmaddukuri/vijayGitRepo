from pprint import pprint as pp

class Alpha:
    def pprint(self):
        print('pprint from the class Alpha')


class Beta:
    def pprint(self):
        print('pprint from the class Beta')


class Charlie(Beta, Alpha):
    def pprint(self):
        super().pprint()


if __name__ == '__main__':
    Charlie().pprint()
    print()
    pp(Charlie.mro())  # method resolution order
