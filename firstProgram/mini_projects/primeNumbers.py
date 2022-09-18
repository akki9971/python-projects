def is_prime(number): # a function to find a number is prime or not
    i = 2
    while number > 1:
        if i == number:
            return number
            break
        elif number % i == 0:
            return
            break
        else:
            i += 1
            continue

initial_range = int(input("from where to start: "))
finalRange = int(input("where to stop: "))
givenRange = range(initial_range, finalRange + 1)
primeNums = []
for num in givenRange:
    x = is_prime(num)
    if type(x) == int:
        primeNums.append(x)
for x in primeNums:
    print(f"Prime number is {x}".format(x))