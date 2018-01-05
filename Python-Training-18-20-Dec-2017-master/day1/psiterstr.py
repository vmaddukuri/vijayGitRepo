s = 'this is a sample in python'

# iterator
column_count = 0

for item in s:
    if item not in 'aeiou ':
        print("{} : {}".format(item, ord(item)), end='\t\t')
    else:
        print('**', end='\t\t')

    column_count += 1

    if column_count == 10:
        print()
        column_count = 0