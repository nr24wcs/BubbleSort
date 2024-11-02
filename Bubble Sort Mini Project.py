from array import array

def bubble(arr):
    indexing_length = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


print(bubble([6, 8, 9, 2, 35, 87]))



