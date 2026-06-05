def merge_sort(list):
    """
    Sorts a list in ascending order
    Return a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recusively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublist
    Returns two sublist - left and right
    """

    mid = len(list)// 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two list (arrays), sorting them in the process
    Returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sort(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sort(list[1:])

num = [32, 41, 51, 12, 63, 37, 73, 13, 56]
l = merge_sort(num)
print(verify_sort(num))
print(verify_sort(l))


