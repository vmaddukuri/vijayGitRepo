mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mat[1][1] = 'x'
mat[2].append(10)
mat.insert(1, ['a', 'e', 'i'])


for row in mat:
    for item in row:
        print(item, end='\t')
    print()

