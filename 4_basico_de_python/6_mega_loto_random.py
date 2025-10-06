import random

def loto_facil():
    x = sorted(list(random.sample(range(1,26),15)))
    print(x)
def mega_sena():
    x = sorted(list(random.sample(range(1,61),6)))
    print(x)

while True:
    option = int(input("Put 1 to megasena, 2 to lotofacil and 3 to exit: "))
    match option:
        case 1:
            mega_sena()
        case 2:
            loto_facil()
        case 3:
            break
        case _:
            print("Put 1, 2 or 3 to choose an option!")