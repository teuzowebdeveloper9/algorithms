#busca binaria algoritimo
def search_binary(array,item,begin = 0,end = None)
if end is None:
  end = len(array)-1
 if begin <= end:
   quite = (begin + end)//2
   if array[quite] == item:
     return quite
     if item < array[quite]:
       return search_binary(array,item,begin,quite-1)
       else:
         search_binary(array,item,quite + 1,end)
         return None
        
 array = [2,3,6,10,11,15,17,20,25,33,44,99,110,135,145,175,899,999,1001]
 
 search_binary(array,899,len(array)-1)
