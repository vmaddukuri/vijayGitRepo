import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'alpha':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1')  # sort by values
print (sorted_df)
print()

sorted_df = unsorted_df.sort_index()  # sort by row heading
print (sorted_df)
print()

sorted_df = unsorted_df.sort_index(axis=0)  # sort by column heading
print (sorted_df)
