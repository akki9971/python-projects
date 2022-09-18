a = range(0,10)
b = range(1,11)
while True:
    for x in a:
        for y in b:
            if y < 10:
                print(str(x) + str(y), end=' ')
            else:
                print(str((x+1)*y))
    break