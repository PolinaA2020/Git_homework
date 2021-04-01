#ЦАП

import RPi.GPIO as GPIO
import time
import numpy as np
import math
import matplotlib.pyplot as plt




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
    print("Введите число (-1 для выхода):")
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
    print("Введите число повторений:")
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
    #freq = 5 # частота сигнала
    #sample_freq = 1000 #частота дискретизации
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
    from scipy.io import wavfile
    #data_dir = pjoin(dirname(scipy.io.__file__), 'tests', 'data')
    #wav_fname = pjoin('SOUND.wav')
    samplerate, data = wavfile.read('/home/student/Desktop/Git_homework/SOUND.WAV')
    print("samplerate ", samplerate)
    print("data ", data)
    time = 10
    ndarray = np.arange(0, time, 1 / samplerate)


############################################################################

for i in chan_list:
        GPIO.output(i, 0)
#1first_script()
#second_script()
#third_script()
fourth_script()

