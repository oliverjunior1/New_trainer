import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [15,25,20,14,24,31]

z = pd.Series(x,y)
plt.plot(x,y)
plt.show()