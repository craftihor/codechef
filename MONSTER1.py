for i in range(int(input())):
    H,X,Y = tuple(map(int,input().split()))
    if Y >= X :
        print(0)
    else:
        print(1)
