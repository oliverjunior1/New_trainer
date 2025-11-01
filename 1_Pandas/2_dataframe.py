import pandas as pd
import matplotlib.pyplot as plt

x = pd.DataFrame([1,7,9,5,12])
y = pd.DataFrame([0,15,30,45,60])

plt.plot(y, x)
plt.show()