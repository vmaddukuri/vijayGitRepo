# Accessing Data from Series with Position
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print(s[0])
print(s[-3])
print(s[:3])


# Retrieve Data Using Label (Index)
print(s['a'])
print(s[['a','c','d']])
print()