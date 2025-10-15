import matplotlib.pyplot as plt

a = [1,2,3,4,5]
b = [15,12,10,16,15]

plt.plot(a, b)
plt.title("Gráfico em linha")
plt.xlabel("Horas")
plt.ylabel("variações de temperatura")
plt.show()