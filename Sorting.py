import time
def Print(list,pType,length,height,speed):
    for i in range(speed):
        time.sleep(0.001)
    box = " "
    row = " "
    if pType == 2:    
        for row_n in range(height):
            for space in range(length):
                if list[space] >= (height - row_n):
                    row = row + "*"
                else:
                    row = str(row) + " "
            box = box + row
            box = box + '\n'
            row = ""
        box = str(box) + str("*" * length) 
    else:
        for i in list:
            if len(str(i)) == 1:
                box = str(box) + str(i) + "  "
            else:
                box = str(box) + str(i) + " "
    
            
    print box
    
def bubble_sort_p(list,speed,pType):
    length = len(list)
    
    not_sorted = True 
    while not_sorted:
        
        changes = False
        for i in range(length-1):
             
            if list[i] > list[i+1]:
                temp_no = list[i] #temp_no is the higher number
                list[i] = list[i+1]
                list[i+1] = temp_no #We change both of the places 
                changes = True
                if pType == 1:
                    print str("   "* i) + " |  |"
                else:
                    print str(" "* i) + "||"

                Print(list,pType,length,length,speed)                              
            else:
                pass
        if changes == False:
            not_sorted = False
    return list 

def bubble_sort(list):
    length = len(list)
    not_sorted = True 
    while not_sorted:
        changes = False
        for i in range(length-1):
             
            if list[i] > list[i+1]:
                temp_no = list[i] #temp_no is the higher number
                list[i] = list[i+1]
                list[i+1] = temp_no #We change both of the places 
                changes = True
                #print str(" "* i) + "||"                
            else:
                pass
        if changes == False:
            not_sorted = False
    return list 


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
def ins_p(list,pType,speed): 
    
    for i in range(len(list)):#for (the place) of every number in list
        list[:i] = inlist(list[:i],list.pop(i)) # sort(the first part of the list (until where we have sorted) and the next space in the list ) and add it to the second part of the list
        Print(list,pType,len(list),len(list),speed)
    return list 
def merge_sort(list,start,end):
    middle = (end-start)/2 + start
    if middle == start:
        return list 
    else:
        list[start:middle] = merge_sort(list,start,middle)[start:middle]
        list[middle:end] = merge_sort(list,middle,end)[middle:end]
        
        alist = []
        fnum = start
        snum = middle
        while fnum < (middle) and snum < (end):
            if list[fnum] < list[snum]:
                alist.append(list[fnum])
                fnum += 1
            else:
                alist.append(list[snum])
                snum += 1
        if fnum == middle:
            for i in range(snum,end):
                alist.append(list[i])
        elif snum == end:
            for i in range(fnum,middle):
                alist.append(list[i])
        else:
            print "something probably went wrong"
        list[start:end] = alist
        return list
def merge_sort_p(list,start,end,pType,speed):
    middle = (end-start)/2 + start
    if middle == start:
        return list 
    else:
        list[start:middle] = merge_sort_p(list,start,middle,pType,speed)[start:middle]
        list[middle:end] = merge_sort_p(list,middle,end,pType,speed)[middle:end]
        
        alist = []
        fnum = start
        snum = middle
        
        
        while fnum < (middle) and snum < (end):
            if list[fnum] < list[snum]:
                alist.append(list[fnum])
                fnum += 1
            else:
                alist.append(list[snum])
                snum += 1
        if fnum == middle:
            for i in range(snum,end):
                alist.append(list[i])
        elif snum == end:
            for i in range(fnum,middle):
                alist.append(list[i])
        else:
            print "something probably went wrong"
        list[start:end] = alist
        Print(list,pType,len(list),len(list),speed)
        return list


def cocktail_shaker(list):
    length = len(list)
    not_sorted = True 
    print length
    
    while not_sorted:
        changes = False
        for i in range(0,length-1): #for the size of the list -1 (beside the last)
            num1 = i 
            num2 = i + 1 #We mark the next place as well
            if list[num1] > list[num2]: #if the place on the left is larger 
                list = change(list,num1,num2) #we switch the places of the pieces
                changes = True #we mark that there were changes
            else:
                pass
        for i in range(0,length-1): #we run i for every number in the list (except the last one)
            num1 = length - i -2 #for the length of the list -i -2 (the opposite of the list -2 and -1 was just ridiculously confusing )
            num2 = length - i -1
            if list[num1] > list[num2]:
                list = change(list,num1,num2)
                changes = True
            else:
                pass
        if changes == False:
                not_sorted = False 
        
    return list 
def cocktail_shaker_p(list,pType,speed):
    length = len(list)
    not_sorted = True 
    print length
    while not_sorted:
        changes = False
        
        for i in range(0,length-1): #for the size of the list -1 (beside the last)
            num1 = i 
            num2 = i + 1 #We mark the next place as well
            if list[num1] > list[num2]: #if the place on the left is larger 
                list = change(list,num1,num2) #we switch the places of the pieces
                Print(list,pType,length,length,speed)
                changes = True #we mark that there were changes
            else:
                pass
        for i in range(0,length-1): #we run i for every number in the list (except the last one)
            num1 = length - i -2 #for the length of the list -i -2 (the opposite of the list -2 and -1 was just ridiculously confusing )
            num2 = length - i -1
            if list[num1] > list[num2]:
                list = change(list,num1,num2)
                Print(list,pType,length,length,speed)
                changes = True
            else:
                pass
        if changes == False:
                not_sorted = False 
        
    return list 
def change(list,num1,num2):
    temp_no = list[num1]
    list[num1] = list[num2]
    list[num2] = temp_no
    return list