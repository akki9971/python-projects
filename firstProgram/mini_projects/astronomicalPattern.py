# x = int(input("enter number: "))
# y = input("enter 0 or 1: ")
# z = bool(int(y)) # convert 0 or 1 to boolean
# # print(z)
# if z:
#     for x in range(x+1):
#         # print(x)
#         if x > 0:
#             print("+" * x)
# else:
#     for x in range(x+1).__reversed__():
#         # print(x)
#         if x > 0:
#             print("+" * x)

x = int(input("enter number: "))
y = int(input("enter 0 or 1: "))
if y:
    for x in range(1, x+1):
        print("* " * x)
else:
    for x in range(x, 0, -1):
        print("* " * x)


# for x in range(8,0,-1):
#     print(x)
