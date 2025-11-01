import pandas as pd
import matplotlib.pyplot as plt

x = pd.DataFrame([1,7,5])
y = pd.DataFrame([10,20,30])

plt.plot(y, x)
plt.show()