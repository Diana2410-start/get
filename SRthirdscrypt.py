import RPi.GPIO as GPIO
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

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

f = 440*8
sf = 1/44000
t = np.arrange(0,1,sf)
amplitude = 255 * (np.sin(2*math.pi*f*t) +1) // 2

for i in range (0,8,1):
    GPIO.setmode(GPIO.BCM)
    n = D[i]
    GPIO.srtup(n, GPIO.out)
    GPIO.output(n,0)

for i in amplitude:
    binc(int(i))
    time.sleep(sf)

except KeyboardInterrupt:
    print("Error")
finally:
    for x in range (8):
        GPIO.output (reb[x],0)
    GPIO.cleanup()
