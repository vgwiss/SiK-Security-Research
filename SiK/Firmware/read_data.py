import serial
import time
import random

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=0, dsrdtr=False, rtscts=False, xonxoff=False)

data = ""
f = open('output.txt', 'w')
while True:
    bytesToRead = ser.inWaiting()
    line = ser.read(bytesToRead)
    f.write(line)
    time.sleep(0.5)

now = time.time()
for i in range(0, 500):
    ser.write('AAAAAAAAAA')
    time.sleep(0.2)
    print('write A')
    end = time.time()
    if(end - now >= 1):
        #print('HERE!')
        now = time.time()
        bytesToRead = ser.inWaiting()
        print(bytesToRead)
        line = ser.read(bytesToRead)
        split_line = line.split(",")
        for element in split_line:
            if element == '':
                split_line.remove(element)
        if len(split_line) != 0:
            print(split_line)
        f.write(str(len(split_line)) + ',')