numbers = []
file = open('numbers.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    clean = line.strip()
    numbers.append(int(clean))

def merge_sort(values):
    if len(values) <= 1:
        return values
    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])
    right_value = merge_sort(values[middle_index:])
    sort_value = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left_values) and right_index < len(right_value):
        if left_values[left_index] < right_value[right_index]:
            sort_value.append(left_values[left_index])
            left_index += 1
        else:
            sort_value.append(right_value[right_index])
            right_index += 1
    sort_value += left_values[left_index:]
    sort_value += right_value[right_index:]
    return sort_value

print(merge_sort(numbers))