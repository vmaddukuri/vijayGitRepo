"""xs = [1, 2, 3, 4]
ns = [2, 4, 6, 8]

#for item in map(lambda x, n: x ** n, xs, ns):
#    print(item)


items = ['PAM', 'eva', 'title', 'neil', 'nick', 'PAT']

# print("PAM".isupper())
# print(str.isupper('PAM'))

for item in filter(str.isupper, items):
    print(item)"""


import re
pattern = 'bash$'

for m_line in filter(lambda line: re.search(pattern, line, re.I), open('/etc/passwd')):
    print(m_line, end='')