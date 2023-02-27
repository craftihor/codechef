t = int(input())

while t > 0:
    m,n = map(int,input().split())
    tot = m*n*(m+1)*(n+1)//4
    sub = m*n
    print(tot-sub)
    t-=1
