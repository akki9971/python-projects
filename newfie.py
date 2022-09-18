# import math
# # Defining a positive infinite integer
# positive_infinity = int(math.inf)
# # print('Positive Infinity: ', positive_infinity)
# for i in range(0, positive_infinity):
#     print(i)
 
# # Defining a negative infinite integer
# # negative_infinity = float('-inf')
# # print('Negative Infinity: ', negative_infinity)



for i in range(0, 9):
    globals()[f"my_variable{i}"] = 0


print(globals())
# Hello from variable number 3!
