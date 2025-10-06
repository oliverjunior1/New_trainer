# decorations with method
def fun1(x):
    def fun2(*args, **kwargs):
        print("############################")
        x(*args, **kwargs)
        print("############################")
    return fun2

@fun1
def greetings(name):
    print(f"Hello {name}")

greetings("Joaquim")