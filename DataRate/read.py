import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=0, dsrdtr=False, rtscts=False, xonxoff=False)
#clear input buffer
ser.reset_input_buffer()
f = open('GCS_UAS_3_modified.txt', 'w')
count = 0
packets = 0
#start = time.time()
while count < 60:
    time.sleep(1)
   # ser.write("RTS3=25\r\n")
    bytesToRead = ser.inWaiting()
    f.write(str(bytesToRead) + ',')
    print(count, bytesToRead)
    ser.read(bytesToRead)
    count = count + 1
    
#f = open('output.txt', 'wb')
#while(1):
#    data = ser.read(1)
#    f.write(data)
#f.close()
