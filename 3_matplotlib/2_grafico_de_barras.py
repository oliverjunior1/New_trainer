import matplotlib.pyplot as plt

temp = [19, 15, 18, 22, 28, 32]
horas = [4,5,8,10,12,15]

plt.plot(horas, temp)
plt.xlabel("Temperatura em ºC", color='red')
plt.ylabel("Horas do dia", color='blue')
plt.title("Horas do dia x Temperatura", color="skyblue")

plt.show()