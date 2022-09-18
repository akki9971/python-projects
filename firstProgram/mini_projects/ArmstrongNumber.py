n = input("Enter your digit number the number to check Armstrong ")
# print(len(n),type(len(n)))
var = 0
# for i in n:
# 	var += pow(int(i),len(n))
while True:
	for i in n:
		var += pow(int(i), len(n))
	if var == int(n):
		print("yes, Number "+n+" is armstrong number")
		confirm = input("want to check another one type y for yes ")
	else:
		print("no, Number "+n+" is not armstrong number")
		confirm = input("want to check another one type y for yes ")
	if confirm == "y" or confirm == "Y":
		var = 0
		n = input("Enter your digit number the number to check Armstrong ")
		continue
	elif confirm == "n" or confirm == "N":
		print("thanks for coming")
		break
	else:
		print("please type your confirmation as per direction")
		confirm = input("want to check another one type y for yes ")
		continue


# a = int(n[0:1])
# b = int(n[1:2])
# # y = "y"
# while True:
# 	# if y == "y":
# 		if (a**2+b**2) == int(n):
# 			print("yes")
# 			y = input("y to try again")
# 		else:
# 			print("No")
# 			y = input("y to try again")
# 		continue
# 	# else:
# 		break

# def addition(x,y):
# 	a = x + y
# 	# print(a)
# 	return a

# print(a)

# def multi(x,y):
# 	return x * y

# y = addition(False,False)
# print(y)

# print(multi(2,9))