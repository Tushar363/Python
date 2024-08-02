def partition(array,low,high):
    Pivot = array[low]
    i=low
    for j in range(i+1,high+1):
        if array[j]<= Pivot:
            i = i+1
            (array[i],array[j]) = (array[j],array[i])
    array[i],array[low] = array[low],array[i]
    return i
def QuickSort (array,low,high):
    if(low<high):
        mid = partition(array,low,high)
        QuickSort(array,high,mid-1)
        QuickSort(array,mid+1,high)
    return array
data=[1,7,4,1,10,9,-2]
size= len(data)
result = QuickSort(data,0,size-1)
print(result) 