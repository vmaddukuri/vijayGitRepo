# Singleton/BorgSingleton.py
# Alex Martelli's 'Borg'

# borg's singleton class, all object state shared
class Borg:  # singleton class
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    def __init__(self, arg):
        super().__init__()
        self.val = arg  # __dict__

    def __str__(self):
        return self.val

x = Singleton('sausage')
print(x)
y = Singleton('eggs')
print(y)
z = Singleton('spam')
print(Borg._shared_state)
x.val = 'pip'
'''print(id(z.__dict__))
print(id(z.__dict__))
print(id(z.__dict__))'''
print(Borg._shared_state)

