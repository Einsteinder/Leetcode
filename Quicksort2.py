def quicksort(lst,l,r):
    if l < r:
        pivot = partition(lst, l, r)
        quicksort(lst,l,pivot-1)
        quicksort(lst,pivot+1,r)

def partition(lst,l,r):
    pivot = lst[r]
    storeIndex = l
    for i in range(l,r):
        if lst[i] < pivot:
            lst[storeIndex],lst[i] = lst[i], lst[storeIndex]
            storeIndex += 1
    swap(lst,storeIndex,r)
    return storeIndex
def swap(arr,l,r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp
a = [1,4,5,6,2,3,5,7,82,4]
quicksort(a,0,len(a)-1)
print(a)