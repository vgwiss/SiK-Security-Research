import serial
import time
import random
start = time.time()
ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=0, dsrdtr=False, rtscts=False, xonxoff=False)
while True:
    print("+++")
    ser.write("+++")
    time.sleep(0.2)
    ser.write("+++")
    time.sleep(0.2)
    ser.write("+++")
    time.sleep(0.2)
    if ser.inWaiting() > 0:
        data = ser.read(ser.inWaiting())
        if "OK" in data or "+++" in data:
            break
#clear input buffer
ser.reset_input_buffer()
f = open('output.txt', 'w')
count = 0
start = time.time()
while count <= 1000:
    ser.write("RTS3=25\r\n")
    time.sleep(random.random()*0.5)
    bytesToRead = ser.inWaiting()
    #print(ser.read(bytesToRead))
    if "OK" in ser.read(bytesToRead):
        stop = time.time()
        print(count)
        count = count + 1
        f.write(str(stop-start) +',')
        print(count, str(stop-start))
        time.sleep(0.5)
        start = time.time()
#f = open('output.txt', 'wb')
#while(1):
#    data = ser.read(1)
#    f.write(data)
#f.close()
