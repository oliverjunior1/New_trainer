import random

def mega():
    x = sorted(random.sample(range(1,61),6))
    print(x)
def lotofacil():
    x = sorted(random.sample(range(1,26),15))
    print(x)

while True:
    option = int(input("If you want a luck number for mega put 1, to lotofacil 2, and to exit 3: "))
    match option:
        case 1:
            mega()
        case 2:
            lotofacil()
        case 3:
            break
        case _:
            print("Invalid number.")

