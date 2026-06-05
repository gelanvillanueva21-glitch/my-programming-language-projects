print("1 Million For A House")
money = int(input("Enter Your Credit: "))

if money >= 1000000:
	x = 200000
	y = money - 200000
	print("We've deduct 20% of 1 million in your credit for the downpayment")
elif money >= 50000:
	x = 100000
	y = money - 100000
	print("We've deduct 20% of 1 million in your credit for the downpayment")

	
print("You've Paid " , x)
print("Credit Left ", y)