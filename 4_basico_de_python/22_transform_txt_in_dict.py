dicionario = {}

with open('dados.txt', 'r') as document:
    for linha in document:
        if ':' in linha:
            chave,  valor = linha.strip().split(':',1)
            dicionario[chave.strip()] = valor.strip()

print(dicionario)