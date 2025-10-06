import matplotlib.pyplot as plt
import numpy as np

dados = np.random.randn(1000)

plt.hist(dados, bins=30, color='purple')
plt.title('Histograma')
plt.xlabel('Valor')
plt.ylabel('Frequencia')
plt.show()