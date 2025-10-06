import matplotlib.pyplot as plt
# Crie um gráfico de linha com os seguintes dados de temperatura ao longo do dia

horas = ['6h', '9h', '12h', '15h', '18h', '21h']
temperaturas = [18, 22, 28, 30, 26, 20]

plt.plot(horas, temperaturas)
plt.title("Temperatura ao Longo do Dia")
plt.xlabel("Horas")
plt.ylabel("Temperaturas")
plt.show()