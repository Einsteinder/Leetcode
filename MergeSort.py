def mergeSort(lst):
    if len(lst) < 2:
        return lst
    middle = len(lst)//2
    left = lst[0:middle]
    right = lst[middle:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    return res
a = [2,2,4,6,1,67,7,8,2,3,4,6,1,6,3,2]
print(mergeSort(a))
