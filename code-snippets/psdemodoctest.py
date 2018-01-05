import doctest


def power(x, n):
    """
    >>> power(2, 3)
    8

    >>> power(2, 4)
    16

    >>> power(2, 'peter')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "psdemodoctest.py", line 8, in power
        return x ** n
    TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'

    """
    return x ** n


if __name__ == '__main__':
    doctest.testmod()