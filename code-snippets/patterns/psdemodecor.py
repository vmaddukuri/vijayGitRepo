import paramiko

def logger_decorator(func):
    """a decor to log the arguments and the return of the function"""
    def logger_handler(*args):
        """handle"""
        result = func(*args)
        print("{}, arguments:{} returns: {}".format(func.__name__, args, result))
        return result
    return logger_handler


@logger_decorator
def compute(a, b):
    return {'power': a ** b}



# compute = logger_decor(compute)
print(compute)
print()
print(compute(3, 4))