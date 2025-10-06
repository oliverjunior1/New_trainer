x = open('message3.txt', 'w')

x.write('Jesus is so great!!!')

x.close()

x = open('message3.txt', 'r')
print(x.read())
x.close()