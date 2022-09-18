# # print("hello python")
#
# # from datetime import datetime
# # def cdt():
# #     return datetime.now()
# #
# # print(cdt().date())
# # # print(cdt().day())
# # print(cdt().hour)
# # print(cdt().minute)
#
# # with open('hero.txt', 'w') as file:
# #     x = file.readline()
# #     print(x)
#
# # def func1(greet,*args):
# #     print(args,greet)
# #
# # func1("hello","hi","hey")
# # a = ["a","b","c","d","e"]
# str = "hello this is aaquib"
# strNew = str.split(" ")
# # b = str.split("l")
# # print(b)
# def make_capital(x):
#     if len(x)>2:
#         a = x[0].upper()
#         b = x[1:]
#         return a+b
#     else:
#         return x
# capitalised_str = []
# for i in strNew:
#     capitalised_str.append(make_capital(i))
# final = " ".join(capitalised_str)
#
# print(final)

# a = [10,20]
# b = [30,40]
# c = [50,60]
# d = [70,80]
# e = [90,100]
# for i in b:
#     a.append(i)
# c = a+b
# b.append(a)
# print(a)

# def fun():
#     x=100
#     return x
# x = fun() + 1
# print(x)

# lis = ["2","5","10","15"]
# for i in range(len(lis)):
#     lis[i]=int(lis[i])
#     # print(i)
# print(lis)

x = 4.199999999999999999999999999
pennies = x * 100
print(pennies)