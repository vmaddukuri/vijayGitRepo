def argument_logger(func):
    """Decorator"""
    def logger_handler(*args, **kwargs):
        """Decorator Handler"""
        return_value=func(*args)
        print("args: {} returns: {}".format(args, return_value))
        return return_value
    return logger_handler

@argument_logger
def power(x,n):
    return x ** n

print(power(4,5))