for _ in range(int(input())):
    a,b,x,y = tuple(map(int,input().split()))
    if x>y:
        if a %(x-y) == 0:
            t = a//(x-y)
        else:
            t=a//(x-y) +1
        if b > (t*y):
            print(1)
        else:
            print(0)
    else:
        print(0)
