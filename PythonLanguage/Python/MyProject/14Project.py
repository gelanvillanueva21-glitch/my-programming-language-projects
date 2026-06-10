Phone_Num = input("Phone: ")

Number_Digit = {
		"1": "One",
		"2": "Two",
		"3": "Three",
		"4": "Four",
		"5": "Five",
		"6": "Six",
		"7": "Seven",
		"8": "Eight",
		"9": "Nine",
		"0": "Zero"
}

output = " "
for Nums in Phone_Num:
	output += Number_Digit.get(Nums,  "!") + " "
print(output)