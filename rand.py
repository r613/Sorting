from random import randint
def randy(num):
    clist = []
    flist = range(1,num+1)
    for i in range(len(flist)):
        clist.append(flist.pop(randint(0,len(flist)-1)))
    return clist