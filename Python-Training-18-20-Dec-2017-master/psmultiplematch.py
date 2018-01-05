import re

s = 'the python and the perl scripting'
pattern = 'P.+?N'  # non-greedy

m = re.search(pattern, s, re.I)

if m:
    print("match :", m.group())  # match string 
    before = s[:m.start()]
    after = s[m.end():]
    print("before : |{}|".format(before))
    print("after: |{}|".format(after))
else:
    print('failed  to match')