t= int(input())
while t>0:
    a,b,c = map(int,input().split())
    li = [a,b,c]
    a=max(li)
    li.remove(a)
    if a == sum(li):
        print("Yes")
    else:
        print("No")
    t-=1
