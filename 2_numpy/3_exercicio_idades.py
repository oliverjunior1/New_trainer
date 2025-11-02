import numpy as np
# Crie um array com as idades de 10 pessoas e:
# - Calcule a média das idades.
# - Filtre quem tem mais de 30 anos.
# - Crie um array com o dobro das idades.

idade = [42,4,13,39,50,73,49,9,12,17]
idade_acima_de_30 = []

def media():
    media = np.mean(idade)
    print(f'A média das idades é: {media}')
def age_up_to_30():
    for age in idade:
        if age>30:
            idade_acima_de_30.append(age)
        else:
            pass
    print(f'As idades acima dos 30, são: {idade_acima_de_30}')

def dobrar_idades():
    twice_ages = [x*2 for x in idade]
    print(f"O dobro das idades é: {twice_ages}")

media()
age_up_to_30()
dobrar_idades()

