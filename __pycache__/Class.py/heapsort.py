def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for j in range(n - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, j, 0)

    return arr

print(heapSort([2, 3, 1, 5]))

