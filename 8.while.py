i = int(input("Enter number: "))
while True:
	if i < 100:
		i = int(input("Enter number again: "))
		# print("print again: ")
		continue
	print("Congratulations century crossed")
	break