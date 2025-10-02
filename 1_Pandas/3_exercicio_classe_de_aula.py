import pandas as pd
# Crie um DataFrame com dados de alunos (nome, nota, presença) e:
# 1. 	Filtre os alunos com nota maior que 7.
# 2. 	Adicione uma coluna “Aprovado” com base na nota.
# 3. 	Exporte para CSV.

alunos = pd.DataFrame({
    'nome':["Joaquim", 'Alyne', 'Mariane', 'Pepe'],
    'nota':[5,9.2, 9.8,7.5],
    'presenca':[True, True, True, True]
})
for x,y in zip('nome', 'nota'):
    if alunos['nota']>=7.0:
        print(alunos['nota'])