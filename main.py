from Randomify import Input
from Randomify import creator
import time

def Print(list,length,largest,speed):
    for i in range(speed):
        time.sleep(0.001)
    box = " "
    row = " "
    for row_n in range(largest):
        for space in range(length):
            
            
            if list[space] >= (largest - row_n):
                row = row + "*"
            else:
                row = str(row) + " "
        box = box + row
        box = box + '\n'
        row = ""
    box = str(box) + str("*" * length) 
    print box
    


def bubble_sort(list):
    length = len(list)
    speed = Input("Please enter the speed of the program (it will be devided by 1,000)")
    not_sorted = True 
    while not_sorted:
        
        changes = False
        for i in range(length-1):
             
            if list[i] > list[i+1]:
                temp_no = list[i] #temp_no is the higher number
                list[i] = list[i+1]
                list[i+1] = temp_no #We change both of the places 
                changes = True
                print str(" "* i) + "||"
                
                Print(list, length,length,speed)

                
                
            else:
                pass
        if changes == False:
            not_sorted = False
    return list 

list = creator()
print bubble_sort(list)
