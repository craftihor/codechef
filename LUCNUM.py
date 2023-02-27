import math
for i in range(int(input())):
    n = int(input())
    count = 0
    while n%2==0:
        count = count+1 
        n = n//2 
        
    if count%2==0:
        print("1")
    else:
        print("0")
