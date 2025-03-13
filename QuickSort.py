def quicksort(array,start = 0 , end = None):
  if end is None:
    end = len(array)-1
    if start < end:
      pointer = partition(array,start,end )
      quicksort(array,start, pointer -1 )
      quicksort(array,pointer + 1 , end )
def partition(array,start,end):
  pivot = array[end]
  i = start 
  for j in range(start, end):
    if array[j] <= pivot:
      array[j] , array[i] = array[i] , array[j]
      i = i+1
      array[i] , array[end] = array[end] , array[i ]
      return i 
