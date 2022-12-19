import time
import itertools
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
t = 1
GPIO.output(4, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)

def xyak (p) :
    GPIO.output(p, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(p, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(p, GPIO.HIGH)
    time.sleep(t)

def selectNum(i) :
    for j in range(i) :
        xyak(17)
    time.sleep(1)

def selectFullNum(arr) :
    for i in arr :
        selectNum(i)
        moveToNext()
    print("long slepp after invalid")
    time.sleep(7)

def showPassPanel() :
    xyak(4)

def moveToNext() :
    xyak(4)
    time.sleep(2)
            
digits = list(range(0, 10))
startWith = "0052"
for pas in itertools.product(digits, repeat=4):
    if str(pas[0]) + str(pas[1]) + str(pas[2]) + str(pas[3]) >= startWith:
        print(pas)
        showPassPanel()
        selectFullNum(pas)
