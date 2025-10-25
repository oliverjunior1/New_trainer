def args_sum(*args):
    print(sum(args))

# Solicita os números separados por espaço
x = input("Put the numbers, to sum: ")

# Converte a string em uma lista de inteiros
nums = list(map(int, x.split(',')))

# Chama a função com os números como argumentos
args_sum(*nums)