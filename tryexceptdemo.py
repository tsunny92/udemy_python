
def trydemo():
	while True:
		try:
			num1 = int(input("Enter the number: "))
		except:
			print("That is not a number")
			continue
		else:
			print(num1)
			break
		finally:
			print("I will always run")

trydemo()
