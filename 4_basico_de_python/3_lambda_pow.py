while True:
    number1 = int(input("Put the first number: "))
    number2 = int(input("Put the second number: "))
    number3 = int(input("Put the third number: "))

    print(f"The math case is ({number1}-{number2}){number3}. ")

    calculate = lambda a, b, c: (a-b)**c
    print(calculate(number1, number2, number3))






