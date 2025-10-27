import random as rd

def mega():
    x = sorted(rd.sample(range(1,61),6))
    print(x)
def facil():
    x = sorted(rd.sample(range(1,26),15))
    print(x)


while True:
    option = int(input("Type 1 to megasena, 2 to lotofacil and 3 to exit: "))
    match option:
        case 1:
            mega()
        case 2:
            facil()
        case 3:
            break