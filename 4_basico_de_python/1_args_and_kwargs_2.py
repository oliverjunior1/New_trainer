#Do args with arithmetics operations

def soma(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)

soma(10,10,10,10,10)