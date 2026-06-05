upper_word = str(input("Enter Upper Word: "))

if upper_word.isupper():
	print("Your Word Is Upper Case")
	print("You may proceed")
else:
	print("Your word is not Upper")
	
lower_word = str(input("Enter Lower Word: "))

if lower_word.islower():
	print("Your Word Is Lower Case")
	print("You may proceed")
else:
	print("Your word is not lower")
	
print("End Of The Program")