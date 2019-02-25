#v1.3 Much more orginized user gets to choose how to programs works - beginning of something great!
from Randomify import Input
from Randomify import creator
from Sorting import bubble_sort
from Sorting import merge_sort
from Sorting import bubble_sort_p
import time


def menu():
    sort_type =2#Input("What sort type would you like to use? \n 1. Bubble sort (fun to watch) (redicilously slow).\n 2. Merge sort")
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
    if sort_type == 2:
        print merge_sort(list)
    else:
        print "The Program doesn't support that sorting method ...yet"
menu()