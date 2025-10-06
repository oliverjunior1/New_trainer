import matplotlib.pyplot as plt

labels = ['Maçã', 'Banana', 'Laranja', 'Uva']
valores = [30, 25, 20, 25]

plt.pie(valores, labels=labels, autopct='%1.1f%%')
plt.title('Distribuição de Frutas')
plt.show()