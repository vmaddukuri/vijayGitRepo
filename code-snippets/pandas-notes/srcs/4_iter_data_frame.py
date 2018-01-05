import pandas as pd
import numpy as np

N = 20

df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])


for col in df:
    print(col)

print()

"""
To iterate over the rows of the DataFrame, we can use the following functions −

iteritems() − to iterate over the (key,value) pairs

iterrows() − iterate over the rows as (index,series) pairs

itertuples() − iterate over the rows as namedtuples
"""

for key,value in df.iteritems():
   print(key,value)

print()

# iterrows()
# iterrows() returns the iterator yielding each index value along with a series
# containing the data in each row.

for row_index,row in df.iterrows():
   print(row_index,row)

# tertuples() method will return an
# iterator yielding a named tuple for each row in the DataFrame.
for row in df.itertuples():
    print(row)

    