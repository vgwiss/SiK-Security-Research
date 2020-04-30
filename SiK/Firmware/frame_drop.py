import serial
import time
import random

ser = serial.Serial('/dev/ttyUSB1', 57600, timeout=0, dsrdtr=False, rtscts=False, xonxoff=False)

data = ""
f = open('frame.txt', 'w')
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


"""
#clear input buffer
ser.reset_input_buffer()
f = open('output.txt', 'w')
count = 0
packets = 0
#start = time.time()
while count < 1000:
    ser.write("RTS3=25\r\n")
    #time.sleep(random.random()*.5)
    #time.sleep(0.14)
    bytesToRead = ser.inWaiting()
    packets = packets + 1
    if "OK" in ser.read(bytesToRead):
        #ser.reset_input_buffer()
        #ser.reset_output_buffer()
        count = count + 1
        print(count, packets)
        f.write(str(packets) +',')
        packets = 0
        time.sleep(0.5)
"""