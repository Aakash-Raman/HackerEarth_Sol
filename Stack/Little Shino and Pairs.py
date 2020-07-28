'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=int(float(input()))
arr=list(map(float, input().split(' ')))
 
 
count=0
for i in range(n):
    for j in range(i,n):
        if arr[i]<arr[j]:
            count+=1
            break
    for k in range(0,i):
        if arr[i]<arr[k]:
            count+=1
            break
         
print(count)
