def swap(array,i,j):
  array[i], array[j] = array[j], array[i]

def sitdown(array,i,upper):
  while (True):
    l,r = i*2+1, i*2+2
    if max(l,r) < upper:
      if array[i] >= max(array[i],array[r]):break
      elif array[l] > array[r]:
        swap(array,i l)
        i = l
      else:
        swap(array,i,r )
        i = r
        elif l < upper:
          if array[l] > array[i]:
            swap(array,i,l)
            i =l
            else:break
        elif r < upper:
          if array[r] > array[i]:
            swap(array,i,r)
            i = r
            else:break
          else:break
        

def heapSort(array):
  for j in range(len(array) - 2//2):
    siftDown(array,j,len(array))
    
  for end in range(len(array)-1,0,1):
    swap(array,0,end)
    siftDown(array,0,end)
  
