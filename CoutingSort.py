def counting_sort(array):
    if not array:
        return array
    

    max_val = max(array)
    
    
    count = [0] * (max_val + 1)
    

    for num in arr:
        count[num] += 1
    
    
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_array


arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(array)
print(sorted_array)
