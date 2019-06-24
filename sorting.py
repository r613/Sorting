from user import Print
from user import sPrint
def bubble_sort(tlist):
    changed = True
    number = len(tlist)
    print number
    while changed:
        changed = False
        for i in range(len(tlist)-1):
            if tlist[i] > tlist[i+1]:
                temp = tlist[i]
                tlist[i] = tlist[i+1]
                tlist[i+1] = temp
                changed = True
    return tlist

def pbubble_sort(tlist):
    changed = True
    number = len(tlist)
    print number
    while changed:
        changed = False
        for i in range(len(tlist)-1):
            if tlist[i] > tlist[i+1]:
                temp = tlist[i]
                tlist[i] = tlist[i+1]
                tlist[i+1] = temp
                Print(tlist)
                changed = True
    return tlist

def cocktail_shaker(tlist):
    changed = True
    number = len(tlist)
    print number
    while changed:
        changed = False
        jlist =  range(len(tlist)-1)
        for i in jlist:
            if tlist[i] > tlist[i+1]:
                temp = tlist[i]
                tlist[i] = tlist[i+1]
                tlist[i+1] = temp
                changed = True
        jlist.reverse()
        for i in jlist:
            if tlist[i] > tlist[i+1]:
                temp = tlist[i]
                tlist[i] = tlist[i+1]
                tlist[i+1] = temp
                changed = True
    return tlist

def pcocktail_shaker(tlist):
    changed = True
    number = len(tlist)
    print number
    while changed:
        changed = False
        jlist =  range(len(tlist)-1)
        for i in jlist:
            if tlist[i] > tlist[i+1]:
                temp = tlist[i]
                tlist[i] = tlist[i+1]
                tlist[i+1] = temp
                Print(tlist)
                changed = True
        jlist.reverse()
        for i in jlist:
            if tlist[i] > tlist[i+1]:
                temp = tlist[i]
                tlist[i] = tlist[i+1]
                tlist[i+1] = temp
                Print(tlist)
                changed = True
    return tlist

def merge_sort(tlist,p1,p2):
    half = ((p2-p1)/2)+p1
    #print tlist
    #print "p1: {} p2: {} half: {} len(tlist): {}".format(p1,p2,half,len(tlist))
    if half == p1 or half == p2:
        #print "half got somewhere"
        return tlist
    list1 = merge_sort(tlist,p1,half)[p1:half]
    list2 = merge_sort(tlist,half,p2)[half:p2]
    nlist = []
    for i in range(p1,p2):
        if len(list1)>0:
            if len(list2) > 0:
                if list1[0] <= list2[0]:
                    tlist[i] = list1.pop(0)
                else:
                    tlist[i] = list2.pop(0)

            else:
                tlist[i] = list1.pop(0)
        else:
            tlist[i] = list2.pop(0)
    return tlist

def pmerge_sort(tlist,p1,p2):
    half = ((p2-p1)/2)+p1
    #print tlist
    #print "p1: {} p2: {} half: {} len(tlist): {}".format(p1,p2,half,len(tlist))
    if half == p1 or half == p2:
        #print "half got somewhere"
        return tlist
    list1 = pmerge_sort(tlist,p1,half)[p1:half]
    list2 = pmerge_sort(tlist,half,p2)[half:p2]
    nlist = []
    #Print(tlist)
    #print tlist
    for i in range(p1,p2):
        if len(list1)>0:
            if len(list2) > 0:
                #print tlist
                if list1[0] <= list2[0]:
                    tlist[i] = list1.pop(0)
                else:
                    tlist[i] = list2.pop(0)
                Print(tlist)
                #print tlist
            else:
                tlist[i] = list1.pop(0)
                Print(tlist)
        else:
            tlist[i] = list2.pop(0)
            Print(tlist)
    return tlist

def insertion(tlist):
    for i in range(0,len(tlist)):
        for a in range(i):
            if tlist[i] < tlist[a]:
                
                tlist.insert(a,tlist.pop(i))
                break
    return tlist

def pinsertion(tlist):
    for i in range(0,len(tlist)):
        for a in range(i):
            sPrint(tlist,[a,i])
            if tlist[i] < tlist[a]: 
                tlist.insert(a,tlist.pop(i))
                break
        
    return tlist

def selection(tlist):
    for i in range(len(tlist)):
        s = i
        for a in range(i,len(tlist)):
            if tlist[a] < tlist[s]:
                s = a
        tlist.insert(i,tlist.pop(s))
    return tlist

def pselection(tlist):
    for i in range(len(tlist)):
        s = i
        for a in range(i,len(tlist)):
            sPrint(tlist,[a,s])
            if tlist[a] < tlist[s]:
                s = a
        tlist.insert(i,tlist.pop(s))
    return tlist