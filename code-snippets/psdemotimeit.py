from timeit import timeit

def demo1():
    temp = []
    for item in range(100):
        temp.append(hex(item))

    return temp


def demo2():
    return [hex(item) for item in range(100)]

if __name__ == '__main__':
    print(timeit('listdir("/tmp")', setup='from os import listdir', number=10000))
    print(timeit('demo2()', setup='from __main__ import demo2', number=10000))
