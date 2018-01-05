# scope
# global
# local
n = 1000  # global


def demo():
    global n  # refer the global scope of n instead creating a local variable
    n = 'pip'
    print(n)

demo()
print(n)
n = 123.21
print(n)


