import matplotlib.pyplot as plt

frutas = ['Maçã', 'Banana','Laranja', 'Uva']
valores = [30,25,20,25]

plt.pie(valores, labels=frutas, autopct='%1.1f%%')
plt.show()