import matplotlib.pyplot as plt

temp = [19, 15, 18, 22, 28, 32]
horas = [4,5,8,10,12,15]

plt.plot(horas, temp)
plt.xlabel("Temperatura em ºC")
plt.ylabel("Horas do dia")
plt.title("Horas do dia x Temperatura")

plt.show()