from psperson import Person


class Employee(Person):
    def __init__(self, eid, fn, ln):
        self.eid = eid
        # invoke overridden methods
        super().__init__(fn, ln)

    def get_info(self):
        print('employee id :', self.eid)
        super().get_info()


if __name__ == '__main__':
    e = Employee('v4004', 'guido', 'rossum')
    e.get_info()
