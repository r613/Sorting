def ins(list):
  
  for i in range(len(list)):#for (the place) of every number in list
    list[:i] = inlist(list[:i],list.pop(i)) # sort(the first part of the list (until where we have sorted) and the next space in the list ) and add it to the second part of the list
  return list 
    
def inlist(list,num):
  for i in range(len(list)): #for every space in the (sorted part of the) list
    if list[i] > num: #if the number is smaller than this piece in the list 
      list.insert(i,num) #insert the number where it belongs
      return list
    else: #if the number is larger than this piece in the list 
      pass # go on
  #if we got here, the number must be larger than any piece in the list 
  list.append(num) #add the number to the end of the list
  
  return list
list = [3,2,5,1,7,3,9,3,5]
print ins(list)
