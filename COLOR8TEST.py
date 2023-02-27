import math

for _ in range(int(input())):
    n,c1,c2,c3,c4,c5,c6 = tuple(map(int,input().split()))
    print((c1+c2+c3+c4+c5+c6)*math.ceil(n/2))
