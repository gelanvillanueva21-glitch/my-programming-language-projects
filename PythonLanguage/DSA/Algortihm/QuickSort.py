numbers = []
file = open('numbers.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    clean = line.strip()
    numbers.append(int(clean))

def quick_sort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    first_pivot = values[0]
    for value in values[1:]:
        if value <= first_pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quick_sort(less_than_pivot) + [first_pivot] + quick_sort(greater_than_pivot)
    
sorted_num = quick_sort(numbers)
print(sorted_num)
