# 3_dict comprehension with my own dates and four items
x = ['a', 'b', 'c', 'd']
y = [1,2,3,4]

z = {(a, b) for (a, b) in zip(x,y)}

print(z)