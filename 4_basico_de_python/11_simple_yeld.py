def next_yield():
    i = 1
    while True:
        yield i * i
        i += 1
for x in next_yield():
    if x > 100:
        break
    else:
        print(x)