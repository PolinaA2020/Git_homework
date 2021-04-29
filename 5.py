#DAC

import RPi.GPIO as GPIO
import time
import numpy as np
import math

GPIO.setmode(GPIO.BCM)

chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
for i in chan_list:
    GPIO.setup(i, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
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
def lightNumber(number):
    number = int(number)
    registers = decToBinList(number)
    for i in range(8):
        if registers[i] == 1:
            GPIO.output(chan_list[i], 1)
    #time.sleep(1)
    #for i in chan_list:
       # GPIO.output(i, 0)
############################################################################
def first_script():
    for i in chan_list:
        GPIO.output(i, 0)
    print("Enter value (-1 to exit): ")
    a = int(input())

    while(a != -1):
        b = float(float(a) / 256 * 3.3)
        b = format(b, '.2f')
        print(a," = ",b,"V")
        lightNumber(a)
        a = int(input())

        for i in chan_list:
            GPIO.output(i, 0)

    
############################################################################
def second_script():
    for i in chan_list:
        GPIO.output(i, 0)
    #print("Enter -1 to exit: ")
    a = int(input())
    
    #while(a < 1000):
       # a = a+1
    while(1):
        for i in range(0, 255, 1):
            lightNumber(i)
            time.sleep(0.005)
            f = 1
            if(GPIO.input(4) == 0):
                b = float(float(i) / 256 * 3.3)
                b = format(b, '.2f')
                if(f == 1):
                    print("1Digital value: ", i, ", Analog value: ", b, "V")
                    f = 0
                #if(f == 0):
                    #break
            
            for i in chan_list:
                GPIO.output(i, 0)
            if(f == 0):
                break
        
############################################################################
def third_script():
    for i in chan_list:
        GPIO.output(i, 0)
    end = 255
    start = 0
    while(1):
        u = (start + end) / 2

        #print(u, "U")
        lightNumber(u)
        time.sleep(0.005)
        if(GPIO.input(4) == 0):
            end = (start + end) / 2
        if(GPIO.input(4) == 1):
            start = (start + end) / 2
       # print(int(start), int(end))
        if(int(start) == int(end)):
            b = float(float(start) / 256 * 3.3)
            b = format(b, '.2f')
            start = int(start)
            print("Digital value: ", start, ", Analog value: ", b, "V")

            start = 0
            end = 255
#if(GPIO.input(4) == 1):
            
            
            
        for i in chan_list:
            GPIO.output(i, 0)
    for i in chan_list:
        GPIO.output(i, 0)
############################################################################
GPIO.output(17, 1)

#first_script()
#second_script()
#third_script()
for i in chan_list:
    GPIO.output(i, 0)

