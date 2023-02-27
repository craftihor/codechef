for t in range(1,int(input())+1):
        n,p=input().split()
        p=int(p)
        currnum=0
        for i in n[::-1]:
            i=int(i)
            currnum=((currnum*10)+((i**p)%10))
        if currnum%7==0:
            print("YES")
        else:
            print("NO")
