import time

def selectNum(i) :
    for j in range(i) :
        print(j)
        time.sleep(0.5)

def selectFullNum(arr) :
    for i in arr :
        selectNum(i)
        moveToNext()

def showPassPanel() :
    print("Show pass panel")
    time.sleep(0.5)

def moveToNext() :
    print("Move to next num")
    time.sleep(0.5)

def iteratePas() :
    global pas
            

pas = [0,0,0,9]

for i in range(1) :
    print(pas)
    showPassPanel()
    selectFullNum(pas)
