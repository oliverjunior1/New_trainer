import pandas as pd
import matplotlib.pyplot as plt

x = pd.DataFrame([1,7,9,5,3,10])
y = pd.DataFrame([10,20,30,40,50,60])

plt.plot(y,x)

plt.show()