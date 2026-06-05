left_right = input("Right or Left: ").lower()

if left_right == "right":
	print("You Found A Valuable Item")
	print("(• ∆ •)")
elif left_right == "left":
	print("You Found Nothing")
	print("(T - T)")
else:
	print("Wrong Direction")
	
print("The End")