# first project

import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
#GPIO.setup(channel, GPIO.OUT)
chan_list = [21, 20, 16, 12, 7, 8, 25, 24]    # add as many channels as you want!
                       # you can tuples instead i.e.:
                       #   chan_list = (11,12)
#GPIO.setup(chan_list, GPIO.OUT)
for i in chan_list:
    GPIO.setup(i, GPIO.OUT)

###############################################################################
def lightUp(ledNumber, period):
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)
###############################################################################
def lightOff(ledNumber, period):
    GPIO.output(ledNumber, 0)
    time.sleep(period)
    GPIO.output(ledNumber, 1)
###############################################################################
def blink(ledNumber, blinkCount, blinkPeriod):
    for j in range(blinkCount):
        lightUp(chan_list[ledNumber], blinkPeriod)
        time.sleep(blinkPeriod)
###############################################################################
def runningLight(count, period):
    for j in range(count):
        for i in chan_list:
            lightUp(i, period)
############################################################################
def runningDark(count, period):
    for i in chan_list:
        GPIO.output(i, 1)
    for j in range(count):
        for i in chan_list:
            lightOff(i, period)
    for i in chan_list:
        GPIO.output(i, 0)
############################################################################
def decToBinList(decNumber):
    bNumber = np.zeros(8)
    for j in range(8):
        bNumber[j] = decNumber % 2
        decNumber /= 2
    return reverse(bNumber, 8)
############################################################################
def reverse(arr, n):
    r_arr = np.zeros(n)
    for i in range(n):
        r_arr[i] = arr[n - i - 1]
    return r_arr
############################################################################
def lightNumber(number):
    registers = decToBinList(number)
    for i in range(8):
        if registers[i] == 1:
            GPIO.output(chan_list[i], 1)
    time.sleep(3)
    for i in chan_list:
        GPIO.output(i, 0)
############################################################################
def runningPattern(pattern, direction):
    #arr = decToBinList(pattern)
    #for j in range(10):
        #for i in range(8):
            #if arr[i]:
                #lightUp(chan_list[i], 1)
      #  arr = move_array(direction, 1)   
    for i in range(10):
        lightNumber(pattern)
        if direction:
            pattern = pattern >> 1
        else:
            pattern = pattern << 1
############################################################################        

#runningPattern(6, 0)
#lightUp(chan_list[3], 1)
#blink(7, 2, 1)
#runningLight(2, 1)
#runningDark(2, 1)
print(decToBinList(5))
print(bin(5))
lightNumber(5)
#runningPattern(6, 0)

GPIO.cleanup()