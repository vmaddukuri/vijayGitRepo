import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.rand(4))
print(np.random.rand(4))

print(s)
print(s.axes)
print(s.values)