import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
for i in chan_list:
    GPIO.setup(i, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

############################################################################
def num2pins(number):
    number = int(number)
    registers = decToBinList(number)
    for i in range(8):
        if registers[i] == 1:
            GPIO.output(chan_list[i], 1)
    #time.sleep(1)
    #for i in chan_list:
       # GPIO.output(i, 0)
############################################################################
def decToBinList(decNumber):
    bNumber = np.zeros(8)
    for j in range(8):
        bNumber[j] = int(decNumber % 2)
        decNumber = int(decNumber / 2)
    return reverse(bNumber, 8)
############################################################################
def reverse(arr, n):
    r_arr = np.zeros(n)
    for i in range(n):
        r_arr[i] = arr[n - i - 1]
    return r_arr
############################################################################
def adc(measures, r, START_TIME):
    for i in chan_list:
        GPIO.output(i, 0)
    end = 255
    start = 0
    t = 0.005
    i = 0
    fl = 0
    START_TIME = time.time()
    while(r > 0):
        u = (start + end) / 2

        num2pins(u)
        time.sleep(0.005)
        r -= 0.005
        if(GPIO.input(4) == 0):
            end = (start + end) / 2
        if(GPIO.input(4) == 1):
            start = (start + end) / 2
        #print(int(start), int(end))
        if(int(start) == int(end)):
            time.sleep(2*t)
            r -= 2*t
            #b = float(float(start) / 256 * 3.3)
            #b = format(b, '.2f')
            start = int(start)
            #print("Digital value: ", start, ", Analog value: ", b, "V")
            measures.append(start)
            if(start >= 240):
                GPIO.output(17, 0)
                fl = 1
            if(start == 150):
                print(time.time() - START_TIME)
            if(start <= 6 and fl == 1):
                
                return
            start = 0
            end = 255
            
            
            
        for i in chan_list:
            GPIO.output(i, 0)
    
############################################################################
try:
    GPIO.output(17, 1)
    measures = []
    START_TIME = time.time()
    adc(measures, 100, START_TIME)
    sett = np.zeros(2)
    sett[0] = 0.05
    sett[1] = 0.3
    np.savetxt('settings.txt', sett, fmt='%.2f')
    np.savetxt('data.txt', measures, fmt='%d')
    fig = plt.plot(measures)
    plt.show()
    
    


finally:
    for i in chan_list:
        GPIO.output(i, 0)
    GPIO.output(17, 0)
