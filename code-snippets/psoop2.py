class Demo:
    def __init__(self):
        print(self, 'am in constructor')

    def __del__(self):
        print(self, 'getting destroyed')


d = Demo()
d2 = Demo()
del d2  # del d3, d4, d5
print(d)
