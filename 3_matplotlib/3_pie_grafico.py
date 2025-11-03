import matplotlib.pyplot as plt

x = ['python', 'java', 'c#', 'outros']
y = [30,25,20,25]

plt.pie(y, labels=x, "%1.1%%f")

plt.show()