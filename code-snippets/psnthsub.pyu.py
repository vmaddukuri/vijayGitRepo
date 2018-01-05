import re

counter = 0


def nth_replacement(m):
    global counter
    counter += 1

    return ',' if counter == 4 else m.group()


s = 'root:x:0:0:root:/root:/bin/bash'
pattern = ':'

s2 = re.sub(pattern, nth_replacement, s)
print(s2)


def demo():
    counter = 123  #local
    print(counter)

demo()
print(counter)

# help(re.sub)