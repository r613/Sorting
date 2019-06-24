def Input(text):
    try: 
        return input(text)
    except:
        print "Number Only!"
        return Input(text)
def menu():
    length = Input("Please enter the length of your list")
    tlist = []
    for i in range(length):
        tlist.append(Input("Add a number to add to the list: "))
    print tlist
    print bubble_sort(tlist)
def bubble_sort(tlist):
    changed = True
    while changed:
        changed = False
        for i in range(len(tlist)-1):
            if tlist [i] > tlist[i+1]:
                temp = tlist[i]
                tlist[i] = tlist[i+1]
                tlist[i+1] = temp
                changed = True
    return  tlist

menu()
