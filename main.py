#v2.0 now with bubble sort, merge sort and insertion sort and prints them all

from Randomify import creator
from Sorting import bubble_sort

from Sorting import bubble_sort_p

from Sorting import ins
from Sorting import ins_p
from Sorting import merge_sort
from Sorting import merge_sort_p
import time

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

def menu():
    sort_type = Input("What sort type would you like to use? \n 1. Bubble sort (fun to watch) (redicilously slow).\n 2. Merge sort\n 3. Insert")
    list = creator()
    print "This is the list we will be sorting: " + str(list)
    pType = Input("what type of printing would you like to see as the program is running? \n 0. None (Fastest) \n 1. The list itself. \n 2. I nice diagram (Super slow) (Super fun to watch)")
    
    if sort_type == 1:
        if pType == 0:
            print bubble_sort(list)
        
        elif pType == 1 or pType == 2:
            speed = Input("How fast (slow) would you like the program to run? (The program ths amount of milleseconds before each print)")
            print bubble_sort_p(list,speed,pType)
        
        else:
            print "The Program doesn't support that printing type ...yet"
    elif sort_type == 2:
        if pType == 0:
            print merge_sort(list,0,len(list))
        else:
            speed = Input("How fast (slow) would you like the program to run? (The program ths amount of milleseconds before each print)")
            print list
            print "program doesn't support printing... yet"
            print  merge_sort_p(list,0,len(list),pType,speed)
    elif sort_type == 3:
        if pType == 0:
            print ins(list)
        else:
            print ins_p(list,pType,Input("How fast (slow) would you like the program to run? (The program ths amount of milleseconds before each print)"))

    #if sort_type == 4:
     #   print quick(list)
    
    else:
        print "The Program doesn't support that sorting method ...yet"
    
menu()