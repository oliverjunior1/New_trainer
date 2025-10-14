import pandas as pd
import numpy as np

ser = pd.Series()
print("Pandas Series", ser)

data =  np.array(['G', 'e', 'e', 'k', 's'])

ser = pd.Series(data)
print(ser)