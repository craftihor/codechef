for _ in range(int(input())):
    p,x,y,z = tuple(map(int,input().split()))
    if z == 1:
        print(f'{p+(p*(y/100)):.10f}')
    else:
        print(f'{p-(p*(x/100)):.10f}')
