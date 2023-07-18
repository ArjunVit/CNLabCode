mssg = input("Enter the message: ")
k = int(input("Enter the segment size: "))

# Dividing sent message in packets of k bits.
n = int(len(mssg)/k)
c = [mssg[i*k:(i+1)*k] for i in range(n)]

# Calculating the binary sum of packets
s = 0
for i in range(n):
    s += int(c[i], 2)
sum = bin(s)[2:]

# Adding the overflow bits
if(len(sum) > k):
    x = len(sum)-k
    sum = bin(int(sum[0:x], 2)+int(sum[x:], 2))[2:]
if(len(sum) < k):
    sum = '0'*(k-len(sum))+sum

# Calculating the complement of sum
checkSum = ''
for i in sum:
    if(i == '1'):
        checkSum += '0'
    else:
        checkSum += '1'

print("checkSum for the message is: ", checkSum)
'''
1 0 0 1 0 1 0 1
0 1 1 0 0 0 1 1
1 0 0 1 0 1 0 0
1 1 1 0 1 1 0 0
---------------
0 1 1 1 1 0 0 0
            1 0
---------------
0 1 1 1 1 0 1 0
1 0 0 0 0 1 0 1
'''
