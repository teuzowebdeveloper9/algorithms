def mergeSort(array, start=0, end=None):
    if end is None:
        end = len(array)

    if (end - start > 1):
        quite = (end + start) // 2  # 
        mergeSort(array, start, quite)
        mergeSort(array, quite, end)
        merge(array, start, quite, end)

def merge(array, start, quite, end):
    left = array[start:quite]
    right = array[quite:end]
    
    i, j = 0, 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1


    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
