#Do args with arithmetics operations

def args_sum(*args):
    sum =0
    for arg in args:
        sum += arg
    return sum

x =args_sum(10,10,10,10)

print(x)