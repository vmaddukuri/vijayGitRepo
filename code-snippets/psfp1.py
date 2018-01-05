items = [3, 2, 1, 4, 5, 6, 7, 8]

m = map(hex, items)
print(m)

print()
for item in m:
    print(item)


"""m = map(hex, items)
print(m)
# print(hex)
# print(hex(12))
"""
ascii = list(map(ord, 'peter pan'))
print(ascii)