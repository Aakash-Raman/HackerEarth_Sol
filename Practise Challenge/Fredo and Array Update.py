# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
a = []
get = input()
a.append(get.split())
s = 0
for i in range(0,n):
    s += int(a[0][i])
print(int(s/n + 1))
