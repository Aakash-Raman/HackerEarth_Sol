n = int(input())
string = input()
arr = [int(s) for s in string.split(' ')]
i = 0
j = len(arr)-1
while(i < len(arr) and j >= 0):
    A = arr[i]
    B = arr[j]
    if(A < B):
        print('2', end = " ")
        i += 1
    elif(A > B):
        print('1', end = " ")
        j -= 1
    else:
        print('0', end = " ")
        i += 1
        j -= 1

