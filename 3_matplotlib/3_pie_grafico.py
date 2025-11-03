import matplotlib.pyplot as plt

x = ['python', 'java', 'c#', 'outras']
y = [35,25,20,20]

plt.bar(y, labels=x,autopct="%1.1f%%")
plt.show()