import csv
from matplotlib import pyplot as plt
import numpy as np
import statistics

file1 = []
file2 = []
file3 = []
file4 = []
output = []
total = 0
#f= open("timed__hist.txt","w")
with open('random_injected_drone100_wait5_1000.data') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        file1.append(row)
        print("POW")

with open('output.txt') as newfile:
    csvreader = csv.reader(newfile, delimiter=',')
    for row in csvreader:
        file3.append(row)

for x in range(0, len(file1[0])):
    if file1[0][x] != '' and file1[0][x] != '\r\n' and file1[0][x] != '\n':
        file2.append(int(file1[0][x]))
        total += int(file1[0][x])

print(len(file2))
print(sum(file2))
print("avg: ")
print(total/len(file2))
print(statistics.pstdev(file2))
mean = sum(file2) / len(file2) 
variance = sum([((x - mean) ** 2) for x in file2]) / len(file2)
print(variance)
res = variance ** 0.5
print("Res = ", res)
for x in range(0, len(file1[0])):
    if file3[0][x] != '' and file3[0][x] != '\r\n' and file3[0][x] != '\n':
        file4.append(int(file3[0][x]))
        #print(int(file1[0][x]))

"""
for x in range(0, len(file1[1])):
    if file1[1][x] != '' and file1[1][x] != '\r\n' and file1[1][x] != '\n':
        file2.append(int(file1[1][x]))
"""
        #f.write(file1[0][x] + ',\r\n')
#f.close()
#print(len(file2))
#bins = np.arange(1, 2, 1)
#plt.xlim([0, 1])
#print(file2)
print(np.percentile(file2, 90))
(n, bins, patches) = plt.hist(file2, bins=np.arange(0,40,1),facecolor="none", color='black', alpha=0.5,histtype='step', density=True, cumulative=True)
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.grid(color='black',linestyle='dashed', linewidth=0.3)
plt.title('Random Injection Rate [0.0, 0.5] Seconds, N = 1000')
plt.suptitle('Frames Injected Until Exploit')
plt.xlabel('Frames Injected (Bin Size = 1)')
plt.ylabel('Cumulative % Of Successful Exploits')
plt.show()

for number in n:
    print(str(n) + ",")
"""
with open('./Armed_2_Radio2.data', newline='') as csvfile2:
    csvreader = csv.reader(csvfile2, delimiter=',')
    for row in csvreader:
        file2.append(row)

with open('./Armed_2_Radio3.data', newline='') as csvfile3:
    csvreader = csv.reader(csvfile3, delimiter=',')
    for row in csvreader:
        file3.append(row)

for x in range(0, 100):
    avg = (file1[x] + file2[x] + file3[x])/3
    output.append(avg)
    print(avg)
"""
