numbers = [ 5, 6, 7, 8, 9, 5, 6]

for index1 in range(len(numbers)):
	for index2 in numbers:
		if index1 == index2:
			numbers.remove(index1)
print(numbers)