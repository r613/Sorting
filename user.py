import os
import time
speed = 0.5
def Input(text):
    try:
        return input(text)
    except:
        print"Numbers only!"
        return Input(text)
def Print(tlist):
    text = "\n"
    l = len(tlist)
    fspeed = float(speed)/l
    time.sleep(fspeed)
    for rrow in range(l):
        row = "\n"
        
        for column in range(l):
            if tlist[column] >= l-rrow:
               row += " |"
            else:
                row += "  "
        text += row
    os.system("clear")
    print text  

def sPrint(tlist,slist):
    text = "\n"
    l = len(tlist)
    fspeed = float(speed)/l
    time.sleep(fspeed)
    for rrow in range(l):
        row = "\n"
        
        for column in range(l):
            if slist.count(column) == 1:
                if tlist[column] >= l-rrow:
                    row += " *"
                else:
                    row += "  "
            elif tlist[column] >= l-rrow:
               row += " |"
            else:
                row += "  "
        text += row
    os.system("clear")
    print text  
