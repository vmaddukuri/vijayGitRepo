""".iloc()
Pandas provide various methods in order to get purely integer based indexing.
Like python and numpy, these are 0-based indexing.

The various access methods are as follows −

An Integer
A list of integers
A range of values
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print(df.iloc[:4])
print()
print(df.iloc[1:5, 2:4])
print()
print(df.iloc[:4])
print()
print(df.iloc[:4])
print()


print(df.iloc[[1, 3, 5], [1, 3]])
print(df.iloc[1:3, :])
print(df.iloc[:,1:3])   