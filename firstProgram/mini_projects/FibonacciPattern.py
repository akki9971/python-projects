limit  = int(input("enter how many pattern you want to print: "))

# def Fibonacci(n):
#     numbers = []
#     a = 0
#     b = 1
#     x = 1
#     while 1:
#         if len(numbers)<n:
#             numbers.append(a)
#             x = a + b
#             a = b
#             b = x
#             continue
#         else:
#             break
#     return numbers
    
def Fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (Fibonacci(n - 1) + Fibonacci(n - 2))

for i in range(1, limit+1):
    print(Fibonacci(i), end=", ")