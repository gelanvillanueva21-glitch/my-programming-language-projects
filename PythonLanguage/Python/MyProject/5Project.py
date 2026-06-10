create_pass = input("Create Password: ")

confirm_pass = input("Confirm Password: ")

if confirm_pass == create_pass:
	print("You may proceed")
	print("Correct Password")
else:
	print("Wrong Password")

print("Done")