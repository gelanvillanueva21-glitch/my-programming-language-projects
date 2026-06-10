weight = int(input("Weight: "))

weight_converter = str(input("(L)bs or (K)g: "))

if weight_converter.upper() == "L":
	print(f"You are {int(weight / 2.205)} Kg")
elif weight_converter.upper() == "K":
	print(f"You are {int(weight * 2.205)} Lbs")
else:
	print("Hello World")