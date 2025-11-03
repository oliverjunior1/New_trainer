import matplotlib.pyplot as plt

x = ['python', 'java', 'javascript', 'c#', 'outras']
y = [30,20,25,12,13]

plt.title('AS LINGUAGENS MAIS USADAS NO MUNDO', color='blue')
plt.pie(y, labels=x, autopct="%1.1f%%")
plt.show()