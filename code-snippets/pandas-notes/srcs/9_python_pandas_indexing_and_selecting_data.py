
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
    index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print(df.loc[:,'A'])
print()
print(df.loc[:,['A', 'C']])
print()
# Select few rows for multiple columns, say list[]
print(df.loc[['a','b','f','h'],['A','C']])
print()

# Select range of rows for all columns
print(df.loc['a':'h'])
