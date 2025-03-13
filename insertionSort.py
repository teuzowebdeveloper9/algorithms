def insertionSort (array):
  item =len(array)
  for i in range(1,item):
    key = array[i]
    while j >= 0 and array[j] > key:
      array[j + 1]  = array[j]
      j = j - 1
      array[j + 1] = key
