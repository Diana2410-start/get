import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ber=[10, 9 ,11 ,5,6 ,13 ,19, 26]
reb=[26,19,13,6,5,11,9,10]
for n in ber:
    GPIO.setup(n, GPIO.OUT)

def binc(num):
    n=7
    p=0
    X=[]
    while n>0:
        p=int(num/2**n)
        if p== 1:
            X.append(1)
            num-=2**n
        else:
            X.append(0)
        n-=1
    X.append(num)
    return X


def lightNumber(decNumber):
    n=[0,0,0,0,0,0,0,0]
    n=binc(decNumber)
    print(n)
    for i in range(8):
        GPIO.output(reb[i],n[i])
    

try:
    repetitionsNumber = int(input("vvedite: "))
    for i in range (0,repetitionsNumber):
        for i in range(256):
            lightNumber(i)
            time.sleep(0.01)
        for i in range(256):
            lightNumber(255-i)
            time.sleep(0.01)
finally:
    for x in range (8):
        GPIO.output (reb[x],0)
    GPIO.cleanup()



