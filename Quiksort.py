def quickSort(lst):
    if len(lst)<=1:
        return lst
    pivot = lst[0]
    left = []
    equal = []
    right = []
    for i in lst:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    left = quickSort(left)
    right = quickSort(right)
    return left + equal + right
print(quickSort([7,5,7,8,0,2,3,4,51,5,7,8]))