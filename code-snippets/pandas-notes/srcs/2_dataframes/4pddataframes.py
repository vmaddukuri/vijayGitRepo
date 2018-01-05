"""Create DataFrame
A pandas DataFrame can be created using various inputs like −

- Lists
- dict
- Series
- Numpy ndarrays
- Another DataFrame
"""


import pandas as pd
df = pd.DataFrame()  # empty
print(df)

data = [1,2,3,4,5]
df = pd.DataFrame(data)  #from list
print(df)

data = [['Alex',10],['William',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)



data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)


