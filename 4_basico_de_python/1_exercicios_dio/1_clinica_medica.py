# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes com índice de chegada
pacientes = []

# Loop para entrada de dados
for i in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((i, nome, idade, status.strip().lower()))

# Ordenar por prioridade:
# 1) urgente primeiro -> usamos (status != "urgente") (False para urgente, True para non-urgente)
# 2) idade decrescente -> usamos -idade
# 3) ordem de chegada -> usamos o índice i
pacientes_ordenados = sorted(
    pacientes,
    key=lambda p: (p[3] != "urgente", -p[2], p[0])
)

# Gerar a lista de nomes na ordem de atendimento
ordem = [p[1] for p in pacientes_ordenados]

# Exibir o resultado
print("Ordem de Atendimento: " + ", ".join(ordem))
