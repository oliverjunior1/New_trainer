def fun1(x):
    def fun2(*args, **kwargs):
        print("######################")
        x(*args, *kwargs)
        print("######################")
    return fun2

@fun1
def gretings(*args):
    for arg in args:
        print(f"Hello {arg}")

gretings("Joaquim", "Alyne", "Joao", "Mariane")