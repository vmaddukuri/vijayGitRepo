#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

s = pd.Series()
print(s)
print()
data = np.array(['a','b','c','d'])

s = pd.Series(data)
print(s)
print()
s = pd.Series(data, index=[100,101,102,103])
print(s)
print(s[100])

