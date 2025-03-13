array = [1,999,16,17,15,76,809,765]
lenght = len(array)
minValue = 0
for j in range(lenght):
 for i in range(j,lenght):
  if array[i] < array[minValue]:
    minValue = i
    j = 0
    if array[j] > array[minValue]:
      aux = array[j]
    array[minValue] = aux

  


