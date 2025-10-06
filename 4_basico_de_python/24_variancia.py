dados = [10, 12, 23, 23, 16, 23, 21, 16]
media = sum(dados) / len(dados)
variancia = sum((x - media) ** 2 for x in dados) / (len(dados) - 1)
print(f"Variância amostral: {variancia:.2f}")