import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [15,10,20,25,18]

z = pd.Series(y,x)

print(z)
plt.plot(z)

plt.show()
