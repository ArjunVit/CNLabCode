mssg = input("Enter the recieved message with checksum: ")
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

# Calculating the complement of sum
checkSum = ''
for i in sum:
    if(i == '1'):
        checkSum += '0'
    else:
        checkSum += '1'

print("Check sum for the revieced message is: ", checkSum)

if int(checkSum,2) == 0:
    print("STATUS: ACCEPTED")
else:
    print("STATUS: ERROR DETECTED")
#    a = checkSum.count('1')
#    b = 0
#    for i in range(a):
#        b = checkSum.find('1', b+1)
#        print(b)
