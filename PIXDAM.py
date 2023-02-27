import math
for i in range(int(input())):
    H,W,X,Y,K = tuple(map(int,input().split()))
    n = math.sqrt((W-X)**2 + (H-Y)**2)
    if n < K:
        print(1)
    else:
        print(0)
    
