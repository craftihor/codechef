import math
for _ in range(int(input())):
    x,y,z = tuple(map(int,input().split()))
    if z == 1:
        print(-1)
    elif (y % z == 0):
        print(-1)
    else:
        k = math.ceil(((x+0.1)/y))*y
        while(k%z == 0):
            k+=y
        print(k)
