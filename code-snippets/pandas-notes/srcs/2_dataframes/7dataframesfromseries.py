# Create a DataFrame from Dict of Series
# Dictionary of Series can be passed to form a DataFrame.

import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print()
print(  )
# Column Selection
print(df['one'])