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
def merge_sort(list):
    
    if len(list) == 1:
        return list
    
    else:
        nlist = []
        flist = merge_sort(list[:len(list)/2])

        slist = merge_sort(list[len(list)/2:])
        
        go = True
        while go:
            
            if len(flist)== 0:
                
                for i in slist:
                    nlist.append(i)
                return nlist
                
            if len(slist) == 0:

                for i in flist:
                    nlist.append(i)
                return nlist
            else:
                
                
                if flist[0] > slist[0]:
                    nlist.append(slist.pop(0))
                else:
                    nlist.append(flist.pop(0))
    return nlist
            
    