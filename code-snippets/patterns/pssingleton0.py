class OnlyOne(object):
    class __SingletonImplementation(object):
        def __init__(self):
            self.val = None



    instance = None

    def __new__(cls): # __new__ always a classmethod
        print cls
        print
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__SingletonImplementation()
        return OnlyOne.instance

x = OnlyOne()
x.val = 'item1'
print(x.val)
y = OnlyOne()
y.val = 'item2'
print y
print id(x)
print id(y)