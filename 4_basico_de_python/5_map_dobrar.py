def dobrar(x):
    return x**2

a = [10,20,30,40]
y = map(dobrar, a)

print(list(y))