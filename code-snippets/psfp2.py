ascii = [112, 101, 116, 101, 114, 32, 112, 97, 110]


def tag_it(av):
    return '<ascii char="{}">{}</ascii>'.format(chr(av), av)


m = map(tag_it, ascii)
m = map(lambda av: '<ascii char="{}">{}</ascii>'.format(chr(av), av), ascii)


for tag in m:
    print(tag)