import serial
import time
import random

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=0, dsrdtr=False, rtscts=False, xonxoff=False)

data = ""
while True:
    print("+++")
    ser.write("+++")
    time.sleep(0.1)
    ser.write("+++")
    time.sleep(0.2)
    ser.write("+++")
    time.sleep(0.3)
    if ser.inWaiting() > 0:
        data = ser.read(ser.inWaiting())
    if "OK" in data or "+++" in data:
        break
#clear input buffer
ser.reset_input_buffer()
f = open('output.txt', 'w')
count = 0
packets = 0
#start = time.time()
while count < 1000:
    ser.write("RTS3=25\r\n")
    time.sleep(random.random()*.5)
    #time.sleep(0.10)
    bytesToRead = ser.inWaiting()
    packets = packets + 1
    if "OK" in ser.read(bytesToRead):
        #ser.reset_input_buffer()
        #ser.reset_output_buffer()
        count = count + 1
        print(count, packets)
        f.write(str(packets) +',')
        packets = 0
        time.sleep(1)
