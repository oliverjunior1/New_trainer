import pandas as pd
import matplotlib.pyplot as plt

x = pd.Series([15,17,25,18,17,26])

plt.plot(x)
plt.title("TEMPERATURA/DIAS")
plt.ylabel('temperatura')
plt.xlabel('dias')
plt.show()

