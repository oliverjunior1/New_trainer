import matplotlib.pyplot as plt

meses = ['janeiro', 'março', 'maio', 'julho', 'agosto']
chuvas = [100,80,40,70,150]

plt.title("Chuva por época do ano:", color='blue')
plt.bar(meses, chuvas, color='pink')
plt.xlabel('Meses do ano', color= 'green')
plt.ylabel('ml/m² de chuva', color="red")

plt.show()