# Python program for implementation of Quicksort Sort

# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[low]

	# pointer for greater element
	i = low 
	for j in range(i+1, high+1):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	array[i], array[low] = array[low], array[i]

	# Return the position from where partition is done
	return i

# function to perform quicksort


def quickSort(array, low, high):
        if( low < high):
            
            mid = partition(array,low,high)
            quickSort(array,low,mid-1)
            quickSort(array,mid+1,high)
            
        return array
    


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

result = quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')

print(result)