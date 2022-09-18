divisor = int(input("[+] Enter your Divisor: "))
divident = int(input("[+] Enter your Divident: "))


def doubleslash(divisor_param, divident_param):
    values = []
    if divisor_param == 0:
        values.append({"remainder": "undefind", "quotient": "infinite"})
        return values[len(values) - 1]

    i = 0
    while True:
        if (divisor_param * i) <= divident_param:
            x = divident_param - (divisor_param * i)
            values.append({"remainder": x, "quotient": i})
            i += 1
            continue
        else:
            break
    return values[len(values) - 1]


math_problem = doubleslash(divisor, divident)
print(math_problem)
