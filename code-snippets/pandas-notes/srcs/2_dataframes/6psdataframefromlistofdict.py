# Create a DataFrame from List of Dicts

import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

# create a DataFrame by passing a list of dictionaries and the row indices.

data = [{'a': 1, 'b': 2, },{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second', ])
print(df)
print()

# create a DataFrame with a list of dictionaries, row indices, and column indices.

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

print(df1)


