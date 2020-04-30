import csv
import statistics
from matplotlib import pyplot as plt
import numpy as np
file1 = []
file2 = []
file3 = []
file4 = []
output = []
total = 0
#f= open("timed__hist.txt","w")
with open('output.txt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        file1.append(row)
        print("POW")

for x in range(0, len(file1[0])):
    if file1[0][x] != '':
        file2.append(round(float(file1[0][x]),2))
        #f.write(file1[0][x] + ',\r\n'a)
        total += round(float(file1[0][x]),2)
print("avg: ")
print(total/len(file2))
print(statistics.pstdev(file2))

listOfStrings2 = [.9 for i in range(1000)]
print(np.percentile(file2, 10))
weights = np.ones_like(file2)/len(file2)
weights2 = np.ones_like(file4)/len(file4)
plt.hist(file4, bins=np.arange(0, 25, 0.1), weights=weights2, histtype='step',facecolor="none", color='blue', edgecolor='blue',linewidth=1.0, alpha=0.5, normed=False, cumulative=True, label='Modified Attacker')
plt.hist(file2, bins=np.arange(0, 25, .01), weights=weights, histtype='step',facecolor="none", color='red', edgecolor='red', lw=1.0, alpha=0.5, normed=False, cumulative=True, label='Unmodified Attacker')
#plt.hist(file2, bins=np.arange(0, 20, .3), alpha=0.5, normed=True, cumulative=True)
listOfStrings2 = [.9 for i in range(1000)]
plt.grid(color='black', linestyle='dashed', linewidth=0.3)
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.suptitle('Time Elapsed Until Exploit')
plt.title('Random Injection Rate [0.0, 0.5] Seconds, N = 1000')
plt.xlabel('Time Elapsed From First Injection (Bin Size = 0.01) (seconds)')
plt.ylabel('Cumulative % Of Successful Exploits')
plt.legend(loc=4)

plt.show()

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
