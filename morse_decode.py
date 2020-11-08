import pyaudio
import struct
import math
from datetime import datetime
from time import time

thresh = 0.002
sample_period = 0.01
RATE = 44100
sample_cycles = int(RATE*sample_period)
SHORT_NORMALIZE = (1.0/32768.0)

CHANNELS = 2
FORMAT=pyaudio.paInt16

def rms(sample):
    count = len(sample)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, sample )

    sum_squares = 0.0
    for i in shorts:

        n = i * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )

pa=pyaudio.PyAudio()

stream = pa.open(format = FORMAT,                      
         channels = CHANNELS,                          
         rate = RATE,                                  
         input = True,                                 
         frames_per_buffer = sample_cycles)

thresh_final=thresh
list1=""
counter=0
start_time = time()
for i in range(100):
    try:
        sample=stream.read(sample_cycles)
    except IOError:
        print("Error Recording")

    amp=rms(sample)

    if amp>thresh:
        list1+="1"
    else:
        list1+="0"
end_time = time()
seconds_elapsed = end_time - start_time
print(seconds_elapsed)
list1=list1.split("0")
print(list1)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

n=len(list1)

i=0
while(i<n):
    if (i != 0 and list1[i]=='' and not hasNumbers(list1[i-1])):
        list1[i-1]=list1[i-1]+' '
        list1[i:]=list1[(i+1):]
        n-=1
    else:
        i+=1

for i in range(len(list1)):
    if not hasNumbers(list1[i]) and len(list1[i])>25:
        print(" ", end='')
    elif len(list1[i])>25:
        print ("Dah", end='')
    elif len(list1[i])>5 and len(list1[i])<17:
        print("Dit", end='')
        
print('end!')