while True:
    a = float(input("Put a number: "))
    b = float(input("Put another number: "))
    c = float(input("Put other number: "))

    calculo = lambda x,y,z: (x**y)**z

    print(calculo(a, b, c))






