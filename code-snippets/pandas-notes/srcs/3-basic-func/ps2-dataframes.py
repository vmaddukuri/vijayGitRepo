import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:")
print(df)
print()
print(df.T)  # transpose
print()

# axes
# Returns the list of row axis labels and column axis labels.
print ("Row axis labels and column axis labels are:")
print(df.axes)
print()


# ndim
# Returns the number of dimensions of the object. By definition, DataFrame is a 2D object.
print(df.ndim)
print()

#shape
print(df.shape)
print()

#values
# Returns the actual data in the DataFrame as an NDarray.
print(df.values)
print()
# Head & Tail, To view a small sample of a DataFrame object,
print(df.head(1))
print()
