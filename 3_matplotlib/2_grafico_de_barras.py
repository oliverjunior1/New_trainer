import matplotlib.pyplot as plt

meses = ['janeiro', 'abril', 'julho', 'outubro', 'dezembro']
temperatura_media = [15,20,22,30,25]

plt.bar(meses, temperatura_media, color='lightblue')
plt.title("Temperatura Media Durante os Meses do Ano", color='blue')
plt.xlabel('Meses')
plt.ylabel('Temperatura')


plt.show()