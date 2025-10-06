def args_sum(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(args_sum(10,10,10,10,10))
