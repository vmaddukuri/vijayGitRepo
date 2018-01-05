import numpy as np
import sys

# python numpy is that it occupies less memory as compared to list. 

S = range(1000)
print(sys.getsizeof(5) * len(S))

D = np.arange(1000)
print(D.size * D.itemsize)