
def odd_even_num(input_number):
	if input_number % 2 == 0:
		if input_number == 0:
			print("Your Number Is A Zero")
		else:
			print(input_number ,"Is an Even Number")
	else:
		print(input_number ,"Is an Odd Number")
	if input_number > 0:
			print("Is A Positive Number")
	else:
			print("Is A Negative Number")
	

try:
	print("Input A Number")
	input_number = int(input("> "))
	odd_even_num(input_number)
	
except ValueError:
	print("Input An Integer Value")