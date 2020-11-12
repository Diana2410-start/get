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
   
    #for x in range (8):
        #GPIO.output (reb[x],0)


try:
     m=10
     while m>5:
         x = input("vvedi  ")
         a=int(x)
         if a ==-1:
             break
         if a>-1 and a<256:
             lightNumber(a)
except KeyboardInterrupt:
     print("Error 404")
except ValueError:
     print("Error 404")
finally:
    
    for x in range (8):
        GPIO.output (reb[x],0)
    GPIO.cleanup()
    