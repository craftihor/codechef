for _ in range(int(input())):
    n,c = tuple(map(int,input().split()))
    r1 = 0
    summ =0
    for i in range(n):
        r2 = int(input())
        if r1 == 1 or r2 == 1 :
            summ+=c
        r1 = r2
    print(summ)
