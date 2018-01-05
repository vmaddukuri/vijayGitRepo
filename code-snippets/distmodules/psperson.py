class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    def get_info(self):
        print('first name :', self.fn)
        print('last name :', self.ln)


if __name__ == '__main__':
    p = Person('larry', 'wall')
    p2 = Person('jimmy', 'nickson')
    p.age = 3
    p.gender = 'male'

    print(p.__dict__)
    print(p2.__dict__)
    #print(__name__)
