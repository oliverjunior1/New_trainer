import random

import pandas as pd
# Crie um DataFrame com dados de alunos (nome, nota, presença) e:
# 1. 	Filtre os alunos com nota maior que 7.
# 2. 	Adicione uma coluna “Aprovado” com base na nota.
# 3. 	Exporte para CSV.

import pandas as pd

# 1️⃣ Criar o DataFrame
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Nota': [8.5, 6.0, 7.2, 9.0, 5.5],
    'Presenca (%)': [95, 80, 88, 98, 70]
}

df = pd.DataFrame(dados)

# 2️⃣ Filtrar alunos com nota maior que 7
aprovados = df[df['Nota'] > 7]

# 3️⃣ Adicionar coluna "Aprovado"
df['Aprovado'] = df['Nota'] >= 7

# 4️⃣ Exportar para CSV
df.to_csv('alunos_resultado.csv', index=False)

# 5️⃣ Exibir os resultados
print("📊 DataFrame completo:")
print(df)

print("\n✅ Alunos com nota acima de 7:")
print(aprovados)


