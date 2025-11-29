import pandas as pd
import matplotlib.pyplot as plt

x = pd.DataFrame(range(10))
y  = pd.DataFrame(range(20))

y = plt.plot(x, y)

plt.show()