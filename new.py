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
def adc(r):
    for i in chan_list:
        GPIO.output(i, 0)
    end = 255
    start = 0
    measures = []
    i = 0
    while(r > 0):
        u = (start + end) / 2

        #print(u, "U")
        num2pins(u)
        time.sleep(0.005)
        r -= 0.005
        if(GPIO.input(4) == 0):
            end = (start + end) / 2
        if(GPIO.input(4) == 1):
            start = (start + end) / 2
        #print(int(start), int(end))
        if(int(start) == int(end)):
            time.sleep(0.1)
            r -= 0.1
            b = float(float(start) / 256 * 3.3)
            b = format(b, '.2f')
            start = int(start)
            #print("Digital value: ", start, ", Analog value: ", b, "V")
            measures.append(float(b))
            start = 0
            end = 255
            
            
            
        for i in chan_list:
            GPIO.output(i, 0)
    
    return measures
############################################################################
try:
    GPIO.output(17, 1)
    measures = adc(15.0)
    print(measures)
    fig = plt.plot(measures)
    plt.show()
    np.save('data1.npy', measures) 
    GPIO.output(17, 0)
    measures = adc(15.0)
    print(measures)
    


finally:
    for i in chan_list:
        GPIO.output(i, 0)
    GPIO.output(17, 0)
    #np.savetxt('data.txt', measure, fmt='%d')