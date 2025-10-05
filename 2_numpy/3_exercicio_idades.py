import numpy as np
# Crie um array com as idades de 10 pessoas e:
# - Calcule a média das idades.
# - Filtre quem tem mais de 30 anos.
# - Crie um array com o dobro das idades.

idade = [42,4,13,39,50,73,49,9,12,17]

media = np.mean(idade)
print(f"A média das idades é: {media}")

def filtro_idade():
    for i in idade:
        if i>=30:
            print(f"A pessoa com {i} anos tem mais de 30.")
        else:
            pass

filtro_idade()

dobro_das_idades = [x*2 for x in idade]

print(f"O dobro das idades é: {dobro_das_idades}")



