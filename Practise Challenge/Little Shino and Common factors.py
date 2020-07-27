# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import math
# Write your code here
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
a, b = map(int,input().split())
n = gcd(a,b)
ctr = 0
for i in range(1, int(math.sqrt(n))+1):
    if(n % i == 0):
        if(n / i == i):
            ctr += 1
        else:
            ctr += 2
print(ctr)
