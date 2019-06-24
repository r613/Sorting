
from rand import randy
from user import Input
from user import Print
from user import sPrint
from sorting import bubble_sort
from sorting import pbubble_sort
from sorting import cocktail_shaker
from sorting import pcocktail_shaker
from sorting import merge_sort
from sorting import pmerge_sort
from sorting import insertion
from sorting import pinsertion
from sorting import selection
from sorting import pselection
def menu():
    length = Input("What would you like the size of your list to be?")
    tlist = randy(length)
    
    #for i in range(length):
    #    tlist.append(Input("Please enter a number to add to your list: "))
    print tlist
    choice = Input("""Which sorting method would you like to use?
    1.  Bubble Sort
    10. Bubble Sort     - Live
    2.  Cocktail Sort
    20. Cocktail Sort   - Live
    3.  Merge Sort
    30. Merge Sort      - Live
    4.  Insertion sort
    40.  Insertion sort - Live
    5.  Selection Sort
    50. Selection Sort  - Live""")
    if choice == 1:
        print bubble_sort(tlist)
    elif choice == 10:
        Print(pbubble_sort(tlist))
    elif choice == 2: 
        print cocktail_shaker(tlist)
    elif choice == 20:
        Print(pcocktail_shaker(tlist))
    elif choice == 3:
        print merge_sort(tlist,0,len(tlist))
    elif choice == 30:
        Print(pmerge_sort(tlist,0,len(tlist)))
    elif choice == 4:
        print insertion(tlist)
    elif choice == 40:
        Print(pinsertion(tlist))
    elif choice == 5:
        print selection(tlist)
    elif choice == 50:
        print pselection(tlist)
    elif choice == 60:
        print quick(tlist)
    else:
        print "That sorting algorithm doesn't exist yet"


def quick(tlist):
    if tlist == []:
        return tlist
    if len(tlist) == 1:
        return tlist
    half = len(tlist)/2
    tlist.append(tlist.pop(half))
    list1 = []
    list2 = []
    for i in range(len(tlist)-2):
        if tlist[i] < tlist[len(tlist)-1]:
            list1.append(tlist[i])
        else:
            list2.append(tlist[i])
    
    list1 = quick(list1)
    list2 = quick(list2)
    print tlist[len(tlist)-1]
    print list1 + [tlist[len(tlist)-1]] + list2
    return list1 + [tlist[len(tlist)-1]] + list2



menu()