import RPi.GPIO as GPIO
import time
import numpy as np
import math
#import matplotlib.pyplot as plt

import scipy.io.wavfile as sc




GPIO.setmode(GPIO.BCM)
#chan_list = [10, 9, 11, 5, 6, 13, 19, 26]
chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
for i in chan_list:
    GPIO.setup(i, GPIO.OUT)

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
    time.sleep(0.1 / 10)
    #for i in chan_list:
       # GPIO.output(i, 0)
############################################################################
def first_script():
    print("Enter number (-1 to exit)")
    value = int(input())
    while(value != -1):
        for i in chan_list:
            GPIO.output(i, 0)
        lightNumber(value)
        value = int(input())
    for i in chan_list:
            GPIO.output(i, 0)
############################################################################
def second_script():
    print("Enter number of repeating")
    repet = int(input())
    for i in range(repet):
        for n in range(0, 255, 1):
            lightNumber(n)
            for i in chan_list:
                GPIO.output(i, 0)
        for n in range(255, 0, -1):
            lightNumber(n)
            for i in chan_list:
                GPIO.output(i, 0)
############################################################################
def third_script(time, freq, sample_freq):
    #time = 2 
    #freq = 5 
    #sample_freq = 1000 
    argument = np.arange(0, time * freq * 2 * math.pi, freq * 2 * math.pi / sample_freq)
    ndarray = np.arange(0, time, 1 / sample_freq)
    for i in range(time * sample_freq):
        ndarray[i] = math.sin(argument[i])

    argument = np.arange(0, time, 1 / sample_freq)
    fig = plt.plot(argument, ndarray)
    plt.show()
    for i in range(time * sample_freq):
        lightNumber(ndarray[i] * 127 + 127)
        for i in chan_list:
            GPIO.output(i, 0)
    
############################################################################
def fourth_script():
    rate, data = sc.read("/home/gr008d/Desktop/w3r3w/SOUND.WAV")
    length = data.shape[0] / rate
    print("length ", int(length), "sec")
    print("channel ", data.shape[1])
    print("samplerate ", rate)
    print("type of data ", type(data[1, 0]))
    
    new = []
    for el in data:
        new.append(int(el[0] // 256) & 255)
    for val in new:
        lightNumber(val)

############################################################################

for i in chan_list:
    GPIO.output(i, 0)
#1first_script()
#second_script()
#third_script()
fourth_script()
